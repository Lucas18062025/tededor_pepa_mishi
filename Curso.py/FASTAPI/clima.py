from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/estado_actual", response_class=HTMLResponse)
def estado_actual():
    tz = pytz.timezone("America/Argentina/Salta")
    ahora = datetime.now(tz)
    hora_actual = ahora.strftime("%H:%M:%S")

    temperatura = "11°C"
    sensacion = "10°C"
    cielo = "Nublado ☁️"
    humedad = "96%"
    viento = "8 km/h 💨"

    html = f"""
    <html>
        <head>
            <title>Estado Actual - Tucumán</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                    line-height: 1.6;
                }}
                .card {{
                    background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    max-width: 500px;
                    margin: auto;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🕒 Hora actual en San Miguel de Tucumán</h2>
                <p><strong>{hora_actual}</strong></p>
                <p>🌡️ <strong>Temperatura:</strong> {temperatura} (Sensación: {sensacion})</p>
                <p>🌥️ <strong>Estado del cielo:</strong> {cielo}</p>
                <p>💧 <strong>Humedad:</strong> {humedad}</p>
                <p>🌬️ <strong>Viento:</strong> {viento}</p>
                <hr>
                <p>🎉 ¡Tu API está más despierta que un mate a las 7 AM!</p>
            </div>
        </body>
    </html>
    """
    return html
