from flask import Flask
import folium
import pandas as pd
import json
import os

app = Flask(__name__)

#CONFIGURACIÓN DE RUTAS (CLAVE PARA PYTHONANYWHERE)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(BASE_DIR, 'DATA_MAPA_FINAL_CON_SCORES.csv')
ARCHIVO_JSON = os.path.join(BASE_DIR, 'parroquias.json')

@app.route('/')
def inicio():
    try:
        # 1. Cargar Datos
        if not os.path.exists(ARCHIVO_DATOS) or not os.path.exists(ARCHIVO_JSON):
            return "ERROR: No encuentro los archivos CSV o JSON. Revisa que estén en la misma carpeta."

        df = pd.read_csv(ARCHIVO_DATOS, dtype={'DPA_PARROQ': str})
        df['DPA_PARROQ'] = df['DPA_PARROQ'].astype(str).str.zfill(6)
        
        # Diccionario para búsqueda rápida
        def formatear_score(valor):
            if pd.isna(valor): return "N/A"
            return f"{valor*100:.4f}%"
        
        df['score_formato'] = df['SCORE_PROBABILIDAD_ALTO'].apply(formatear_score)
        datos_dict = df.set_index('DPA_PARROQ').to_dict('index')

        # 2. Crear Mapa
        m = folium.Map(location=[-1.8312, -78.1834], zoom_start=7)

        # 3. Estilos y Capas
        colores = {
            'Bajo': '#2ecc71',   # Verde
            'Medio': '#f1c40f',  # Amarillo
            'Alto': '#e74c3c'    # Rojo
        }

        def estilo(feature):
            cod_parroquia = feature['properties'].get('DPA_PARROQ', '')
            info = datos_dict.get(cod_parroquia, {})
            riesgo = info.get('PREDICCION_RIESGO', 'Sin Datos')
            return {
                'fillColor': colores.get(riesgo, '#9e9e9e'),
                'color': 'black',
                'weight': 0.5,
                'fillOpacity': 0.7
            }

        # 4. Cargar GeoJSON y Unir datos
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        # Inyectar datos del CSV dentro del GeoJSON para que el popup funcione
        for feature in geojson_data['features']:
            cod = feature['properties'].get('DPA_PARROQ')
            if cod in datos_dict:
                feature['properties']['PREDICCION_RIESGO'] = datos_dict[cod]['PREDICCION_RIESGO']
                feature['properties']['score_formato'] = datos_dict[cod]['score_formato']
            else:
                feature['properties']['PREDICCION_RIESGO'] = 'Sin Datos'
                feature['properties']['score_formato'] = 'N/A'

        folium.GeoJson(
            geojson_data,
            style_function=estilo,
            tooltip=folium.GeoJsonTooltip(
                fields=['DPA_DESPAR', 'DPA_DESCAN', 'DPA_DESPRO'],
                aliases=['Parroquia:', 'Cantón:', 'Provincia:'],
                localize=True
            ),
            popup=folium.GeoJsonPopup(
                fields=['PREDICCION_RIESGO', 'score_formato'],
                aliases=['Nivel de Riesgo:', 'Probabilidad (Alto Riesgo):']
            )
        ).add_to(m)

        # 5. RETORNAR EL HTML
        return m.get_root().render()

    except Exception as e:
        return f"Ocurrió un error en el código: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)