Ejemplos de sockets TCP (servidor echo y cliente)

Archivos:
- `s.py`: servidor simple que venía en tu proyecto (echo).
- `server_improved.py`: servidor TCP mejorado que maneja múltiples clientes con hilos, cierre seguro y logging simple.
- `client.py`: cliente de ejemplo que envía un mensaje y muestra el eco.
- `test_echo.py`: script que lanza el servidor y el cliente para verificar que el echo funciona.

Cómo usar (PowerShell en Windows):

1) Ejecutar servidor manualmente:

```powershell
python .\server_improved.py
```

Si quieres que escuche sólo en la interfaz local cambia HOST en `server_improved.py` a `127.0.0.1`.

2) Ejecutar cliente desde otra terminal:

```powershell
python .\client.py "Hola servidor"
```

3) Ejecutar prueba automatizada (lanza servidor y cliente):

```powershell
python .\test_echo.py
```

Notas y problemas comunes:
- Si usas una IP fija (p. ej. `192.168.100.240` en `s.py`) asegúrate de que esa IP esté asignada a tu máquina y el firewall permita el puerto.
- Para pruebas locales usa `127.0.0.1` o `localhost`.
- Si el puerto está en uso cambia `PORT`.
- Para producción o tráfico inseguro evita escuchar en 0.0.0.0 sin un firewall y considera TLS.

Siguientes pasos recomendados:
- Añadir TLS con `ssl.wrap_socket` o `ssl.SSLContext`.
- Usar `asyncio` para escalabilidad.
- Añadir pruebas unitarias más completas.
