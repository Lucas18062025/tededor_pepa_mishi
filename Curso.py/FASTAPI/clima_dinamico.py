from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def inicio():
    return """
    <html>
        <body>
            <h2>🚀 ¡FastAPI está funcionando!</h2>
            <p>Usá <code>/estado_actual?ciudad=Tucuman</code> para ver el clima real.</p>
        </body>
    </html>
    """

@app.get("/estado_actual", response_class=HTMLResponse)
async def estado_actual(ciudad: str = Query("Tucuman")):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1"

    async with httpx.AsyncClient() as client:
        geo_response = await client.get(geo_url)
        geo_data = geo_response.json()

    if not geo_data.get("results"):
        return f"<h2>❌ No se encontró la ciudad '{ciudad}'</h2>"

    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    nombre_local = location["name"]
    pais = location["country"]

    clima_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weathercode"
    )

    async with httpx.AsyncClient() as client:
        clima_response = await client.get(clima_url)
        clima_data = clima_response.json()

    clima = clima_data["current"]
    temperatura = clima.get("temperature_2m", "N/A")
    viento = clima.get("wind_speed_10m", "N/A")
    codigo_clima = clima.get("weathercode", 0)

    clima_descriptivo = {
        0: "Despejado ☀️",
        1: "Parcialmente nublado 🌤️",
        2: "Nublado ☁️",
        3: "Cubierto 🌥️",
        45: "Neblina 🌫️",
        61: "Lluvia ligera 🌦️",
        71: "Nieve ligera ❄️",
    }.get(codigo_clima, "Clima desconocido 🌍")

    return f"""
    <html>
        <head>
            <title>Clima en {nombre_local}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #e1f5fe;
                    padding: 20px;
                }}
                .card {{
                    max-width: 500px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
                h2 {{
                    color: #0077c2;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>📍 Clima actual en {nombre_local}, {pais}</h2>
                <p>🌡️ <strong>Temperatura:</strong> {temperatura} °C</p>
                <p>🌬️ <strong>Viento:</strong> {viento} km/h</p>
                <p>🌦️ <strong>Estado del cielo:</strong> {clima_descriptivo}</p>
                <hr>
                <p>🎉 ¡Datos en tiempo real gracias a Open-Meteo!</p>
            </div>
        </body>
    </html>
    """
