import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

st.subheader("Filtrar Datos y Captura de Datos")
st.write("El procesamiento de datos a traves de ciencia de Datos usando Streamlit de Python")

dfDatos = pd.read_csv('http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')

#Mostrar tabla de los registros 
#dfDatos=dfDatos[(dfDatos[""])]

st.metric("***Registros Totales***", len (dfDatos))
st.dataframe(dfDatos, use_container_width=True)
