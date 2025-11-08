from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import subprocess
import socket
import platform
import requests
import dns.resolver
import asyncio
from datetime import datetime
import urllib.request
import json

# Reemplaza 'TU_TOKEN' con el token que te dio @BotFather
TOKEN = '8360611459:AAHmDvn3PzUWTVo1iEA8DPLa79AJVci_rQc'

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("👋 Comando /start recibido")
    mensaje = '¡Hola! Soy tu bot de pruebas de pentesting.\n\nEscribe /ayuda para ver los comandos disponibles.'
    await update.message.reply_text(mensaje)
    print("✅ Mensaje de bienvenida enviado")

# Comando /ayuda
async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Comandos disponibles:\n'
        '/start - Iniciar el bot\n'
        '/ayuda - Ver comandos disponibles\n'
        '/hora - Ver la hora actual\n'
        '/miip - Ver tu IP pública y local\n'
        '/wifi - Ver información de redes WiFi\n'
        '/ping <host> - Hacer ping a un host\n'
        '/dns <dominio> - Obtener registros DNS\n'
        '/puertos <host> - Escanear puertos comunes\n'
        '/sistema - Información del sistema\n'
        '/web <url> - Verificar estado de sitio web'
    )

# Comando /hora
async def hora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hora_actual = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f'La hora actual es: {hora_actual}')

# Comando /ping
async def ping_host(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor, proporciona un host. Ejemplo: /ping google.com")
        return
    
    host = context.args[0]
    try:
        # Usando subprocess de manera segura
        if platform.system().lower() == "windows":
            output = subprocess.check_output(["ping", "-n", "4", host], text=True)
        else:
            output = subprocess.check_output(["ping", "-c", "4", host], text=True)
        await update.message.reply_text(f"Resultado del ping a {host}:\n{output}")
    except Exception as e:
        await update.message.reply_text(f"Error al hacer ping a {host}: {str(e)}")

# Comando /dns
async def check_dns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor, proporciona un dominio. Ejemplo: /dns google.com")
        return
    
    domain = context.args[0]
    try:
        resultado = []
        # Verificar diferentes tipos de registros DNS
        for record_type in ['A', 'MX', 'NS', 'TXT']:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                for rdata in answers:
                    resultado.append(f"{record_type}: {rdata}")
            except:
                continue
        
        if resultado:
            await update.message.reply_text(f"Registros DNS para {domain}:\n" + "\n".join(resultado))
        else:
            await update.message.reply_text(f"No se encontraron registros DNS para {domain}")
    except Exception as e:
        await update.message.reply_text(f"Error al consultar DNS: {str(e)}")

# Comando /puertos
async def scan_ports(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("""
❌ Por favor, usa alguna de estas opciones:

1. Escaneo básico (pocos puertos):
/puertos 192.168.1.1

2. Escaneo completo (todos los puertos):
/puertos 192.168.1.1 full

3. Escaneo de rango de puertos:
/puertos 192.168.1.1 1-1024

4. Escaneo de servicios específicos:
/puertos 192.168.1.1 web    (puertos web)
/puertos 192.168.1.1 mail   (puertos email)
/puertos 192.168.1.1 db     (puertos bases de datos)

Usa /miip para ver tus IPs disponibles.
""")
        return
    
    host = context.args[0]
    print(f"🔍 Iniciando escaneo de {host}")
    
    # Verificar si es una IP válida
    try:
        socket.inet_aton(host)
    except socket.error:
        await update.message.reply_text(f"❌ Error: '{host}' no es una dirección IP válida.")
        return
    
    # Definir diferentes conjuntos de puertos
    port_groups = {
        "web": {
            80: "HTTP",
            443: "HTTPS",
            8080: "HTTP-Alt",
            8443: "HTTPS-Alt",
            3000: "Development",
            4000: "Development",
            5000: "Development",
            8000: "Development",
            8888: "Alternative HTTP",
            9000: "Development"
        },
        "mail": {
            25: "SMTP",
            465: "SMTP SSL",
            587: "SMTP TLS",
            110: "POP3",
            995: "POP3 SSL",
            143: "IMAP",
            993: "IMAP SSL"
        },
        "db": {
            3306: "MySQL",
            5432: "PostgreSQL",
            1433: "MSSQL",
            1521: "Oracle",
            27017: "MongoDB",
            6379: "Redis",
            11211: "Memcached"
        },
        "basic": {
            80: "HTTP",
            443: "HTTPS",
            22: "SSH",
            21: "FTP",
            3389: "RDP",
            445: "SMB",
            139: "NetBIOS",
            53: "DNS"
        }
    }
    
    # Determinar qué puertos escanear basado en los argumentos
    scan_type = context.args[1] if len(context.args) > 1 else "basic"
    
    if scan_type == "full":
        ports_to_scan = {i: f"Puerto {i}" for i in range(1, 1025)}
    elif scan_type == "web":
        ports_to_scan = port_groups["web"]
    elif scan_type == "mail":
        ports_to_scan = port_groups["mail"]
    elif scan_type == "db":
        ports_to_scan = port_groups["db"]
    elif "-" in scan_type:
        try:
            start, end = map(int, scan_type.split("-"))
            ports_to_scan = {i: f"Puerto {i}" for i in range(start, end + 1)}
        except:
            ports_to_scan = port_groups["basic"]
    else:
        ports_to_scan = port_groups["basic"]
    
    await update.message.reply_text(f"🔍 Iniciando escaneo de puertos en {host}...")
    
    resultado = []
    total_abiertos = 0
    
    # Probar conexión inicial
    try:
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.settimeout(2)
        test_socket.connect((host, 80))
        test_socket.close()
    except Exception as e:
        await update.message.reply_text(f"""
⚠️ Advertencia: No se pudo establecer conexión inicial con {host}
Esto puede deberse a:
• El host no está accesible
• Un firewall está bloqueando las conexiones
• La IP está fuera de tu red local

¿Deseas continuar con el escaneo? Usa /puertos {host} force para forzar el escaneo.
""")
        if len(context.args) < 2 or context.args[1] != "force":
            return
    
    status_message = await update.message.reply_text("⌛ Escaneando...")
    
    # Intentar detectar el sistema operativo por TTL
    try:
        ttl_probe = subprocess.check_output(["ping", "-n", "1", host], text=True)
        if "TTL=" in ttl_probe:
            ttl = int(ttl_probe.split("TTL=")[1].split()[0])
            os_guess = "Windows" if ttl > 64 else "Linux/Unix"
        else:
            os_guess = "Desconocido"
    except:
        os_guess = "No detectado"

    for port, service in ports_to_scan.items():
        if port % 100 == 0:  # Actualizar progreso cada 100 puertos
            try:
                await status_message.edit_text(f"⌛ Escaneando puerto {port}/{max(ports_to_scan.keys())}...")
            except:
                pass

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        try:
            print(f"Escaneando puerto {port}")
            result = sock.connect_ex((host, port))
            
            if result == 0:
                total_abiertos += 1
                # Intentar detectar la versión del servicio
                try:
                    banner = ""
                    if port in [80, 8080]:
                        r = requests.get(f"http://{host}:{port}", timeout=2)
                        banner = r.headers.get('Server', '')
                    elif port in [443, 8443]:
                        r = requests.get(f"https://{host}:{port}", timeout=2, verify=False)
                        banner = r.headers.get('Server', '')
                    
                    if banner:
                        resultado.append(f"🟢 Puerto {port} ({service}): ABIERTO - Versión: {banner}")
                    else:
                        resultado.append(f"� Puerto {port} ({service}): ABIERTO")
                except:
                    resultado.append(f"🟢 Puerto {port} ({service}): ABIERTO")
            else:
                resultado.append(f"�🔴 Puerto {port} ({service}): cerrado")
                
        except socket.gaierror:
            await status_message.edit_text(f"❌ Error: No se puede resolver el host {host}")
            return
        except socket.error as e:
            resultado.append(f"⚠️ Puerto {port} ({service}): {str(e)}")
        finally:
            sock.close()

    resumen = f"""
📊 Informe de Escaneo para {host}:
━━━━━━━━━━━━━━━━━━━━━━━
🖥️ Sistema Operativo (estimado): {os_guess}
🔍 Total de puertos escaneados: {len(ports_to_scan)}
✅ Puertos abiertos: {total_abiertos}
❌ Puertos cerrados: {len(ports_to_scan) - total_abiertos}

📝 Resultados detallados:
{chr(10).join(resultado)}

🔧 Tipo de escaneo: {scan_type.upper()}
⚠️ Notas:
• Usa '/puertos {host} full' para un escaneo completo
• Algunos puertos pueden estar filtrados por firewalls
• Para más detalle, considera usar NMAP
"""
    await status_message.edit_text(resumen)

# Comando /sistema
async def system_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info = f"""
Sistema Operativo: {platform.system()} {platform.release()}
Versión: {platform.version()}
Arquitectura: {platform.machine()}
Procesador: {platform.processor()}
Nombre del equipo: {platform.node()}
    """
    await update.message.reply_text(info)

# Comando /wifi
async def get_wifi_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("🔍 Comando /wifi recibido")
    await update.message.reply_text("⌛ Obteniendo información de WiFi...")
    
    try:
        print("Ejecutando comando para interfaces...")
        # Obtener información de la red WiFi actual
        current_network = subprocess.run(
            ["netsh", "wlan", "show", "interface"], 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        
        if current_network.returncode != 0:
            raise Exception(f"Error al obtener interfaces: {current_network.stderr}")
        
        print("Ejecutando comando para redes...")
        # Obtener lista de redes disponibles
        available_networks = subprocess.run(
            ["netsh", "wlan", "show", "networks"], 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        
        if available_networks.returncode != 0:
            raise Exception(f"Error al obtener redes: {available_networks.stderr}")
        
        # Procesar la información
        mensaje = "📡 Información de WiFi:\n\n"
        
        # Debug: imprimir salida raw
        print("Salida de interfaces:")
        print(current_network.stdout)
        print("Salida de redes:")
        print(available_networks.stdout)
        
        # Procesar información de la interfaz actual
        if "Estado" in current_network.stdout:
            mensaje += "🔵 Red Actual:\n"
            for line in current_network.stdout.split('\n'):
                if any(key in line for key in ["Nombre de SSID", "SSID", "Estado", "State", "Señal", "Signal", "Canal", "Channel", "Radio", "Autenticación", "Authentication"]):
                    mensaje += f"{line.strip()}\n"
        
        mensaje += "\n📶 Redes Disponibles:\n"
        
        # Procesar redes disponibles
        networks_output = available_networks.stdout
        if "No hay interfaces" in networks_output or "There are no" in networks_output:
            mensaje += "❌ No se encontraron interfaces inalámbricas.\n"
        else:
            current_ssid = None
            for line in networks_output.split('\n'):
                line = line.strip()
                if "SSID" in line and "BSSID" not in line:
                    ssid_value = line.split(':')[1].strip() if ':' in line else line.replace("SSID", "").strip()
                    if ssid_value and ssid_value != "":
                        current_ssid = ssid_value
                        mensaje += f"\n• {current_ssid}\n"
                elif current_ssid and any(key in line for key in ["Señal", "Signal"]):
                    mensaje += f"  📊 {line.strip()}\n"
                elif current_ssid and any(key in line for key in ["Autenticación", "Authentication"]):
                    mensaje += f"  🔒 {line.strip()}\n"
        
        # Si no encontramos información
        if len(mensaje.split('\n')) <= 3:
            mensaje += "\n❌ No se pudo encontrar información detallada de las redes WiFi."
            mensaje += "\nEsto puede deberse a:\n"
            mensaje += "• No hay adaptador WiFi disponible\n"
            mensaje += "• El adaptador WiFi está desactivado\n"
            mensaje += "• Se requieren permisos de administrador\n"
        
        await update.message.reply_text(mensaje)
        print("✅ Información WiFi enviada")
        
    except Exception as e:
        error_msg = f"""❌ Error al obtener información WiFi:
Detalles: {str(e)}

Esto puede deberse a:
• No hay adaptador WiFi
• El adaptador está desactivado
• Se requieren permisos de administrador

Prueba:
1. Verifica que el WiFi está encendido
2. Ejecuta el bot como administrador
3. Usa el comando 'netsh wlan show interfaces' en CMD para verificar"""
        
        print(f"Error detallado: {str(e)}")
        await update.message.reply_text(error_msg)

# Comando /miip
async def get_ip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("🔍 Comando /miip recibido")
    mensaje = "📡 Información de IP:\n\n"
    
    try:
        # Obtener IP pública usando diferentes servicios
        servicios_ip = [
            'https://api.ipify.org?format=json',
            'https://api.myip.com',
            'https://api64.ipify.org?format=json'
        ]
        
        ip_publica = None
        for servicio in servicios_ip:
            try:
                print(f"Intentando obtener IP pública desde {servicio}")
                response = requests.get(servicio, timeout=3)
                if 'ipify' in servicio:
                    ip_publica = response.json()['ip']
                else:
                    ip_publica = response.json()['ip']
                break
            except:
                continue
        
        if ip_publica:
            mensaje += f"🌐 IP Pública: {ip_publica}\n\n"
            print(f"✅ IP pública obtenida: {ip_publica}")
        else:
            mensaje += "🌐 IP Pública: No se pudo obtener\n\n"
            print("⚠️ No se pudo obtener la IP pública")
    except Exception as e:
        print(f"❌ Error al obtener IP pública: {str(e)}")
        mensaje += "🌐 IP Pública: Error al obtener\n\n"

    try:
        # Obtener IP local y hostname
        hostname = socket.gethostname()
        mensaje += f"🖥️ Hostname: {hostname}\n"
        print(f"✅ Hostname obtenido: {hostname}")

        # Intentar obtener todas las IPs locales
        mensaje += "🏠 IP(s) Local(es):\n"
        ips_locales = set()
        
        # Método 1: Usando socket básico
        try:
            ip_local = socket.gethostbyname(hostname)
            ips_locales.add(ip_local)
        except:
            pass

        # Método 2: Usando getaddrinfo
        try:
            for info in socket.getaddrinfo(hostname, None):
                if info[0] == socket.AF_INET:  # Solo IPv4
                    ips_locales.add(info[4][0])
        except:
            pass

        # Método alternativo usando socket
        try:
            hostname = socket.gethostname()
            # Obtener todas las IPs asociadas al hostname
            ips = socket.gethostbyname_ex(hostname)[2]
            for ip in ips:
                if not ip.startswith('127.'):  # Excluir localhost
                    ips_locales.add(ip)
        except:
            pass

        if ips_locales:
            for ip in sorted(ips_locales):
                mensaje += f"   • {ip}\n"
            print(f"✅ IPs locales obtenidas: {', '.join(ips_locales)}")
        else:
            mensaje += "   • No se encontraron IPs locales\n"
            print("⚠️ No se encontraron IPs locales")

    except Exception as e:
        print(f"❌ Error al obtener IPs locales: {str(e)}")
        mensaje += "   • Error al obtener IPs locales\n"

    # Agregar instrucciones de uso
    mensaje += "\n📝 Para escanear puertos usa:"
    mensaje += "\n/puertos <IP>"
    if ip_publica:
        mensaje += f"\nEjemplo público: /puertos {ip_publica}"
    if ips_locales:
        mensaje += f"\nEjemplo local: /puertos {list(ips_locales)[0]}"

    # Enviar el mensaje
    try:
        await update.message.reply_text(mensaje)
        print("✅ Mensaje enviado correctamente")
    except Exception as e:
        print(f"❌ Error al enviar mensaje: {str(e)}")
        await update.message.reply_text("❌ Ocurrió un error al mostrar la información. Por favor, intenta de nuevo.")
        
    except Exception as e:
        print(f"❌ Error en get_ip: {str(e)}")
        await update.message.reply_text(f"❌ Error al obtener la IP: {str(e)}")

# Comando /web
async def check_website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor, proporciona una URL. Ejemplo: /web https://www.google.com")
        return
    
    url = context.args[0]
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        response = requests.get(url, timeout=5)
        info = f"""
Estado: {response.status_code}
Tiempo de respuesta: {response.elapsed.total_seconds():.2f} segundos
Servidor: {response.headers.get('Server', 'No disponible')}
Contenido-Tipo: {response.headers.get('Content-Type', 'No disponible')}
        """
        await update.message.reply_text(f"Información de {url}:\n{info}")
    except Exception as e:
        await update.message.reply_text(f"Error al verificar {url}: {str(e)}")

# Manejador de mensajes de texto
async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Mensaje recibido: {update.message.text}")  # Debug
    texto = update.message.text.lower()
    print(f"Texto en minúsculas: {texto}")  # Debug
    
    # Diferentes respuestas según el mensaje
    if "hola" in texto:
        print("Respondiendo a saludo")  # Debug
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif "bien" in texto or "todo bien" in texto:
        print("Respondiendo a estado positivo")  # Debug
        await update.message.reply_text("¡Me alegro! ¿En qué puedo ayudarte?")
    elif "?" in texto:
        print("Respondiendo a pregunta")  # Debug
        await update.message.reply_text("Buena pregunta. Déjame ayudarte. Usa /ayuda para ver los comandos disponibles.")
    elif "gracias" in texto:
        print("Respondiendo a agradecimiento")  # Debug
        await update.message.reply_text("¡De nada! Estoy aquí para ayudar.")
    else:
        print("Enviando respuesta por defecto")  # Debug
        await update.message.reply_text("Te escucho. Si necesitas ayuda, usa el comando /ayuda")

def main():
    print("⌛ Iniciando conexión con Telegram...")
    # Crear la aplicación
    app = Application.builder().token(TOKEN).build()
    print("✅ Aplicación creada correctamente")

    print("📝 Registrando comandos...")
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("hora", hora))
    app.add_handler(CommandHandler("ping", ping_host))
    app.add_handler(CommandHandler("dns", check_dns))
    app.add_handler(CommandHandler("puertos", scan_ports))
    app.add_handler(CommandHandler("sistema", system_info))
    app.add_handler(CommandHandler("web", check_website))
    app.add_handler(CommandHandler("miip", get_ip))
    app.add_handler(CommandHandler("wifi", get_wifi_info))
    
    # Registrar el manejador de mensajes de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    # Iniciar el bot
    print("Bot iniciado. Presiona Ctrl+C para detener.")
    
    # Ejecutar el bot
    app.run_polling()

if __name__ == '__main__':
    try:
        print("Iniciando el bot...")
        main()
    except KeyboardInterrupt:
        print("\nBot detenido por el usuario.")
    except Exception as e:
        print(f"Error: {e}")