import requests
import xml.etree.ElementTree as ET
from rich import print
from rich.panel import Panel
from rich.table import Table

# Configuración de Splunk
SPLUNK_HOST = 'https://localhost:8089'
USERNAME = 'admin'
PASSWORD = 'changeme'

# Autenticación y obtención de token
def get_splunk_token():
    url = f"{SPLUNK_HOST}/services/auth/login"
    data = {'username': USERNAME, 'password': PASSWORD}
    response = requests.post(url, data=data, verify=False)
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        session_key = root.find('sessionKey').text
        print(Panel("Autenticación exitosa ✅", title="Splunk Login", style="green"))
        return session_key
    else:
        print(Panel(f"Error autenticando en Splunk:\n{response.text}", title="Error", style="red"))
        return None

# Consulta de búsqueda básica
def splunk_search(query):
    token = get_splunk_token()
    if not token:
        return
    headers = {'Authorization': f'Splunk {token}'}
    search_url = f"{SPLUNK_HOST}/services/search/jobs"
    data = {'search': f"search {query}", 'output_mode': 'json'}
    response = requests.post(search_url, headers=headers, data=data, verify=False)

    if response.status_code == 201:
        job_id = response.json()['sid']
        print(Panel(f"Job creado con ID: {job_id}", title="Búsqueda enviada", style="cyan"))

        # Esperar y obtener resultados
        results_url = f"{SPLUNK_HOST}/services/search/jobs/{job_id}/results?output_mode=json"
        import time
        time.sleep(2)  # Esperar a que el job se procese
        results_response = requests.get(results_url, headers=headers, verify=False)

        if results_response.status_code == 200:
            results = results_response.json()['results']
            if results:
                table = Table(title="Resultados de Splunk", show_lines=True)
                for key in results[0].keys():
                    table.add_column(key, style="bold magenta")

                for row in results:
                    table.add_row(*[str(row.get(k, '')) for k in results[0].keys()])
                print(table)
            else:
                print(Panel("No se encontraron resultados.", style="yellow"))
        else:
            print(Panel(f"Error obteniendo resultados:\n{results_response.text}", style="red"))
    else:
        print(Panel(f"Error creando el job de búsqueda:\n{response.text}", style="red"))

if __name__ == "__main__":
    # Ejemplo de búsqueda
    splunk_search("index=_internal | head 5")
    input("\nPresioná Enter para salir...")