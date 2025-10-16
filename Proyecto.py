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

#presentación
st.markdown(
    """
    <div style="text-align: center; padding: 35px;">
        <h1 style="color:#701705;font-size:75px;margin-bottom: -45px">Proyecto de Análisis de Datos</h1>
        <h1 style="color:#701705;font-size:55px">grupo #1</h1>
        <p style=" font-size:25px; margin-top: 5px">
        <b>Integrantes:</b> 
        </p>
        <p style="font-size:21px; margin-top: -17px;">
         Kevin angel, Maria Paula Iglesias, Esteban Mendez, Maria Cristina Hernandez. 
        </p>
        <p style=" font-size:23px; margin-top: 8px">
            <b>Talento Tech</b> 
        </p>    
                <p style=" font-size:21px ; margin-top: -20px ; margin-bottom: 10px;">
        Análisis de Datos - Explorador 
        </p>
        <p style=" font-size:21px ; margin-top: -15px ; margin-bottom: 10px;">
        Análisis de Datos Explorador - G203P
        </p>
        <p style=" font-size:21px; margin-bottom: 40px;">
        <b>Octubre del 2025</b> 
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Introduccion
st.markdown(
    """
    <div style="text-align: left; padding: 5px;">
        <h1 style="margin-bottom: 20px">Introducción y planteamiento del problema</h1>
        <h4>Contexto:</h4>
        <p style="font-size:16px; margin-top: 8px;">
         El presente proyecto se basa en el análisis del conjunto de datos “DyRET Quadruped Locomotion Dataset”, disponible públicamente en el repositorio de CSIRO Data Portal, el cual nos proporciona un dataset con la recopilación de los datos de una prueba realizada en Brisbane, Australia, en noviembre de 2019 donde se realizaron mediciones en diferentes superficies de dos tipos de sensores (IMU y RAW) en el robot cuadrúpedo DyRET, esta prueba se realizó sobre 6 superficies diferentes a 6 velocidades diferentes.
        </p>
        <p></p>        
        <h4>Importancia:</h4>
        <p style=" font-size:15px;">
        Este análisis contribuye al desarrollo de robots más eficientes y adaptativos, capaces de desplazarse en entornos irregulares, lo cual tiene aplicaciones en:
        </p>
        <ul>
            <li>Exploración de terrenos difíciles (energías renovables, minería, agricultura de precisión).</li>
            <li>Inspección de infraestructuras en zonas de difícil acceso.</li>
            <li>Avances en inteligencia artificial aplicada al control de movimiento.</li>    
        </ul>
        <h4>Problema específico identificado</h4>
        <h4>Preguntas de investigación</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Objetivos
st.markdown(
    """
    <div style="text-align: left; padding: 5px;">
        <h1 style="margin-bottom: 20px">Objetivos</h1>
        <h4>Objetivo general:</h4>
        <p style="font-size:16px; margin-top: 8px;">
         Analizar la relación existente entre la fuerza ejercida por las patas del robot y las características de la superficie sobre la que se desplaza, considerando las variaciones de velocidad y tipo de terreno.
        </p>
        <h4>Objetivos específicos:</h4>
        <ul>
            <li>Comparar las fuerzas realizadas por cada pata y la relación que hay entre ellas durante la marcha.</li>
            <li>Examinar el comportamiento de los componentes de la fuerza (Fx, Fy, Fz) en distintas muestras del sensor raw.</li>
            <li>Definir una hipótesis respecto a la existencia de datos atípicos.</li>    
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)


st.divider()


# Metodología
st.markdown(
    """
    <div style="text-align: left; padding: 5px;">
        <h1 style="margin-bottom: 20px">Metodología</h1>
        <h4>Diseño de la investigación:</h4>
        <p style="font-size:16px; margin-bottom: -0px;">
            <p>El presente proyecto se desarrolló bajo un diseño de investigación aplicada y descriptiva, con enfoque cuantitativo, orientado al análisis, interpretación y visualización de datos provenientes de un conjunto de información (dataset) seleccionado de acuerdo con la temática del curso.</p>
            <p>El propósito principal fue extraer conocimientos relevantes a partir de datos reales mediante técnicas de análisis y minería de datos, el proceso metodológico se estructuró en las siguientes etapas:</p>
            <ol>
                <li>Búsqueda y selección del dataset:</li>
                    <p style="margin-left: 22px;">Se identificó y seleccionó una fuente de datos pertinente al tema de estudio, asegurando su calidad y disponibilidad para el análisis.</p>
                <li>Análisis inicial del tema y exploración de los datos:</li>
                    <p style="margin-left: 22px;">Se realizó una comprensión general y una exploración preliminar de las variables contenidas en el dataset, con el fin de reconocer patrones, valores faltantes y posibles relaciones.</p>
                <li>Organización y limpieza de los datos:</li>    
                    <p style="margin-left: 22px;">Se aplicaron procesos de depuración, transformación y normalización de la información, eliminando registros duplicados, corrigiendo inconsistencias y estandarizando formatos.</p>
                <li>Minería y análisis de datos:</li>
                    <p style="margin-left: 22px;">Se implementaron técnicas estadísticas y de análisis para identificar tendencias, correlaciones y comportamientos significativos dentro del conjunto de datos.</p>
                <li>Visualización y graficación:</li>
                    <p style="margin-left: 22px;">A través de herramientas de análisis de datos se generaron gráficos e indicadores visuales que facilitaron la interpretación de los resultados obtenidos.</p>
                <li>Conclusiones y recomendaciones:</li> 
                    <p style="margin-left: 22px;">Con base en el análisis realizado, se establecieron conclusiones que resumen los hallazgos más relevantes y se formularon recomendaciones orientadas a la mejora de procesos o la toma de decisiones fundamentadas en datos.</p>
            <p>En conjunto, este diseño permitió desarrollar un proceso integral de análisis de datos, desde la adquisición hasta la interpretación final, aplicando las buenas prácticas de la analítica y fortaleciendo las competencias en el uso de herramientas tecnológicas y metodológicas del análisis de información.</p>
            </ol>
        </p>     
        <h4>Fuentes de datos:</h4>
        <p>Los datos utilizados en este proyecto provienen del conjunto de datos público “DyRET Hexapod Locomotion Data”, disponible en el portal de acceso abierto del **Commonwealth Scientific and Industrial Research Organisation (CSIRO)** de Australia.</p>
        <p>Este dataset recopila información experimental obtenida a partir de las pruebas realizadas al robot DyRET (Dynamic Robot for Embodied Testing).</p>
        <h4>Técnicas de análisis utilizadas:</h4>
        <h4>Herramientas tecnológicas:</h4>
        <ul>
            <li>Python</li>
            <li>Seaborn</li>
            <li>Pandas</li>
            <li>Matplotlib.pyplot</li>    
            <li>Streamlit</li>
            <li>Folium</li>
            <li>Streamlit.components.v1</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


#TITULO PRINCIPAL
st.markdown(
    """
    <div style="text-align: center; padding: 5px; margin-top: 50px; ">
        <h1 style="color:#701705;margin-top: -5px;">DyRET Legged Robot Terrain Classification Dataset</h1>
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

#Boton con link
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




#Mapa australia
ciudad = 'Brisbane'
latitud = -37.6167
longitud = 134.3667
mapa = folium.Map(location=[latitud, longitud], zoom_start=4.4,min_zoom=4, max_zoom=18)

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
    gap: 40px;
    margin-top: 25px">
    <div style="flex:1;text-align:center;"
        <p><strong style="font-size: 25px">🦾 Sensores</strong></p>
        <p style="margin-bottom:5px;">- Raw: Sensor de 3 ejes en cada pata (Optoforce OMD-20-SH-80N).</p>
        <p style="margin-bottom:30px;">- IMU: Giroscopio, acelerómetro y magnetómetro de 3 ejes (Xsens MTI-30).</p>
        <p><strong style="font-size: 25px">🌍 Superficies</strong></p>
        <p style="margin-bottom:30px;">Hormigón, césped, grava, mulch, tierra, arena.</p>
        <p><strong style="font-size: 25px">⚙ Velocidades y pasos</strong></p>
        <p>- Velocidades: </p>
        <p style="margin-bottom:5px;">0–1: 0.125 Hz, 2–3: 0.1875 Hz, 4–5: 0.25 Hz.</p>
        <p style="margin-bottom:5px;">- Longitudes de paso: </p> 
        <p style="margin-bottom:30px;">0, 2, 4 → 80 mm; 1, 3, 5 → 120 mm.</p>
    </div>
    <div style="flex:1;text-align:center;"
        <p><strong style="font-size: 25px">🧩 Metadatos</strong></p>
        <p style="margin-bottom:5px;">- Licencia: Creative Commons 4.0</p>  
        <p style="margin-bottom:5px;">- Actualizaciones: No.</p>  
        <p style="margin-bottom:30px;">- Recolección: 10 pruebas por archivo, 8 pasos cada una, en todas las </p>
        <p style="margin-top:-35px;">superficies y velocidades (total: 2880 pasos).</p> 
        <p><strong style="font-size: 25px">🔬 Uso del dataset</strong></p>
        <p style="margin-bottom:5px;">- Validación de modelos cinemáticos/dinámicos.</p>  
        <p style="margin-bottom:30px;">- Clasificación de terreno mediante señales de contacto.</p>
        <p><strong style="font-size: 25px">🎯 Propósito</strong></p>
        <p style="margin-bottom:30px;">Evaluar el rendimiento del robot DyRET según la fuerza aplicada por cada pata</p>
        <p style="margin-top:-35px;">durante la marcha.</p>
    </div>
</div>
""", unsafe_allow_html=True)




st.divider()

#Hito 2
st.markdown(
    """
    <div style="text-align: center; padding: 5px; margin-top: 30px; ">
        <h1 style="color:#701705;margin-top: -5px;">Exploración Inicial de Datos en Python</h1>
        <p style="font-size:16px; margin-top: 10px;">
        <hr style="width:60%; margin: 20px auto;">
        <p style="text-align: center; max-width: 700px; margin: 0 auto; font-size:16px">
            <b>Esta fase se centra en asegurar la calidad de su dataset y en realizar un análisis exploratorio exhaustivo (EDA) para descubrir patrones, 
            anomalías y relaciones iniciales entre las variables.<b>DyRET</b>,
            sobre <b>6 superficies</b> y a <b>6 velocidades</b> diferentes.
        <div style=" justify-content: center; gap: 15px;margin-top: 30px">
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
               ¡Haz clik!
            </button>
        </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

#hito 3
st.markdown(
    """
    <div style="text-align: center; padding: 5px; margin-top: 50px; ">
        <h1 style="color:#701705;margin-top: -5px;">Limpieza y Exploración de Datos con Pandas</h1>
        <p style="font-size:16px; margin-top: 10px;">
        <hr style="width:60%; margin: 20px auto;">
        <p style="text-align: center; max-width: 700px; margin: 0 auto; font-size:16px">
            <b>El objetivo de esta fase es realizar un "chequeo médico" a su dataset. Necesitamos entender su estructura,
             identificar los tipos de variables y detectar posibles problemas (como datos faltantes) desde el principio.<b>DyRET</b>,
            sobre <b>6 superficies</b> y a <b>6 velocidades</b> diferentes.
        <div style=" justify-content: center; gap: 15px;margin-top: 30px">
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
                ¡Haz clik!
            </button>
        </a>   
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.write("")
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
df_proyecto=pd.read_csv('C:\Users\PC\OneDrive\Desktop\Proyecto final análisis de datos\df_qcat_filtrado.csv')



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
