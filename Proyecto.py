import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import folium
from streamlit.components.v1 import html

#Solución al tema claro y tema oscuro de google
st.markdown("""
<style>
:root {
    color-scheme: light dark;
}

/* Estilo base del cuerpo */
body {
    font-family: "Arial", sans-serif;
}

/* Color del texto adaptable */
@media (prefers-color-scheme: light) {
    html, body, [class*="st-"] {
        color: #1e1e1e !important;  /* Texto oscuro en modo claro */
        background-color: #ffffff;
    }
}

@media (prefers-color-scheme: dark) {
    html, body, [class*="st-"] {
        color: #f5f5f5 !important;  /* Texto claro en modo oscuro */
        background-color: #0e1117;
    }
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="Proyecto análisis de datos",
    layout="wide",
    initial_sidebar_state="collapsed"
)

#TITULO PRINCIPAL
st.markdown(
    """
    <div style="text-align: center; padding: 5px;">
        <h1 style="color:#701705;">📊 Proyecto de Análisis de Datos grupo #1</h1>
        <h4 style="margin-top: -5px;">DyRET Legged Robot Terrain Classification Dataset</h4>
        <p style="font-size:16px; margin-top: 10px;">
            <b>Fuente:</b> QCAT de CSIRO
        </p>
        <p style=" font-size:15px;">
            <b>Fecha de publicación:</b> 20 de diciembre de 2020 &nbsp;|&nbsp; <i>No ha tenido actualización</i>
        </p>
        <hr style="width:60%; margin: 20px auto;">
        <p style="text-align: justify; max-width: 700px; margin: 0 auto; font-size:16px">
            <b>Tema:</b> Recopilación de mediciones en diferentes superficies en Brisbane, Australia,
            durante noviembre de 2019, usando dos tipos de sensores del robot cuadrúpedo <b>DyRET</b>,
            sobre <b>6 superficies</b> y a <b>6 velocidades</b> diferentes.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# st.markdown("""
# <style>
# div.stButton > button {
#     display: block;
#     margin: auto;
# }
# </style>
# """, unsafe_allow_html=True)

#LINK "Ir a la pagina principal"
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://www.google.com/url?q=https%3A%2F%2Fdata.csiro.au%2Fcollection%2Fcsiro%3A46885" target="_blank">
            <button style="
                background-color:#701705;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;
            ">
                Ir a la fuente de datos
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")


#Imagen australia
ciudad = 'Brisbane'
latitud = -37.6167
longitud = 134.3667
mapa = folium.Map(location=[latitud, longitud], zoom_start=4.4)

lat=-27.4698
log=153.0251
folium.Marker(
    location=[lat, log],
    popup=f'Marcador en {ciudad}',
    tooltip='Haz clic aquí'
).add_to(mapa)
map_html = mapa._repr_html_()
st.components.v1.html(map_html, height=500)



#Descripcón del proyecto
st.markdown("""
<div style="
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 40px;">
    <div style="flex:1;text-align:justify;"
        <p><strong style="font-size: 25px">🦾 Sensores</strong></p>
        <p style="margin-bottom:5px;">- *Raw:* Sensor de 3 ejes en cada pata (Optoforce OMD-20-SH-80N).</p>
        <p style="margin-bottom:30px;">- *IMU:* Giroscopio, acelerómetro y magnetómetro de 3 ejes (Xsens MTI-30).</p>
        <p><strong style="font-size: 25px">🌍 Superficies</strong></p>
        <p style="margin-bottom:30px;">Hormigón, césped, grava, mulch, tierra, arena.</p>
        <p><strong style="font-size: 25px">⚙ Velocidades y pasoss</strong></p>
        <p>- *Velocidades:* </p>
        <p style="margin-bottom:5px;">0–1: 0.125 Hz, 2–3: 0.1875 Hz, 4–5: 0.25 Hz.</p>
        <p style="margin-bottom:5px;">- *Longitudes de paso:* </p> 
        <p style="margin-bottom:30px;">0, 2, 4 → 80 mm; 1, 3, 5 → 120 mm.</p>
    </div>
    <div style="flex:1;text-align:justify;"
        <p><strong style="font-size: 25px">🧩 Metadatos</strong></p>
        <p style="margin-bottom:5px;">- *Licencia:* Creative Commons 4.0</p>  
        <p style="margin-bottom:5px;">- *Actualizaciones:* No.</p>  
        <p style="margin-bottom:30px;">- *Recolección:* 10 pruebas por archivo, 8 pasos cada una, en todas las superficies y velocidades (total: 2880 pasos).</p> 
        <p><strong style="font-size: 25px">🔬 Uso del dataset</strong></p>
        <p style="margin-bottom:5px;">- Validación de modelos cinemáticos/dinámicos.</p>  
        <p style="margin-bottom:30px;">- Clasificación de terreno mediante señales de contacto.</p>
        <p><strong style="font-size: 25px">🎯 Propósito</strong></p>
        <p style="margin-bottom:30px;">Evaluar el rendimiento del robot DyRET según la fuerza aplicada por cada pata durante la marcha.</p>
    </div>
</div>
""", unsafe_allow_html=True)



st.divider()

#titulo Hito 2
st.markdown("""
    <div style="display: flex; justify-content: center">
        <h1>Hitos</h1>
    </div>
 """,
 unsafe_allow_html=True
)
st.markdown(
    """
    <div style="display: flex; justify-content: center; gap: 15px;">
        <a href="https://colab.research.google.com/drive/1uczDqJNx-5RfNXIooJ5xJSgQ4Cw2fzrs" target="_blank">
            <button style="
                background-color:#701705;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;
            ">
                Ver hito #2
            </button>
        </a>
                <a href="https://colab.research.google.com/drive/1qRZ1FP8FBRl9PFz39juQCs_E4Itvn2lQ" target="_blank">
            <button style="
                background-color:#701705;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;
            ">
                Ver hito #3
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")
st.divider()
st.write("")
st.write("")
st.write("") 


#Titulo drataframe final
st.markdown("""
    <div style="text-align: center; padding: 5px;">
        <h1 style="color:#701705;">📊 Dataframe final</h1>
    </div>
 """,
 unsafe_allow_html=True
)
st.write()


#Importe del dataset final
df_proyecto=pd.read_csv('Proyecto final.csv')



#Filtrar por superficie
st.sidebar.header('Filtros')

superficie=st.sidebar.multiselect(
    'Seleccione superficie',
    options=df_proyecto.Superficie.unique(),
    default=None
)
if superficie:
    df_proyecto = df_proyecto[df_proyecto['Superficie'].isin(superficie)]

st.dataframe(df_proyecto)




#Filtrado por superficie en el Dataframe final

df_concreto_final=df_proyecto[df_proyecto.ID_Superficie== 0]
df_cesped_final=df_proyecto[df_proyecto.ID_Superficie== 1]
df_grava_final=df_proyecto[df_proyecto.ID_Superficie== 2]
df_mantillo_final=df_proyecto[df_proyecto.ID_Superficie== 3]
df_tierra_final=df_proyecto[df_proyecto.ID_Superficie== 4]
df_arena_final=df_proyecto[df_proyecto.ID_Superficie==5]





# Creamos una figura con 4 subgráficos (2 filas x 2 columnas)
fig, axes = plt.subplots(2, 2, figsize=(14,8), sharex=True)

# Lista con las columnas y colores
ejes = [("FL_net", "#E8587A"), ("FR_net", "#E8C658"),
        ("BR_net", "#58C2E8"), ("BL_net", "#7E58E8")]

# Dibujar cada gráfica en su subplot
for ax, (col, color) in zip(axes.flatten(), ejes):
    ax.scatter(df_cesped_final["Velocidad_m_s"], df_cesped_final[col], color=color)
    ax.set_title(f"{col} en función del tiempo")
    ax.set_ylabel("Fuerza")
    ax.set_xlabel("Tiempo_ms (ms)")
    ax.grid(True)

# Etiqueta común del eje X
plt.suptitle("Fuerzas netas por pata en superficie Cesped - Velocidad 1", fontsize=16)
st.pyplot(fig)

