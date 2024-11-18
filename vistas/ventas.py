import streamlit as  st
import pandas as pd
import plotly.express as px





#pip install plotly installar para la conexión de los datos

st.header("Filtrado y Captura de Datos")
st.write("EL procesamiento de datos a través de ciencia de datos usando Streamlit de Python.")

#columnas///
c1, c2, c3 = st.columns(3)

with c1:
    par_nombrePais = st.text_input("Pais:", placeholder="Escribe el nombre de un pais")

with c2:
    par_fertilidad = st.number_input("Minimo de numero de Hijos:", min_value=0, max_value=100, step=1)

with c3: 
    par_rangoExpectativaVida=st.slider("Rango de expectativa de vida:", min_value=10, max_value=100, value=(10,10))


dfDatos = pd.read_csv('https://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')

#Seleccionar datos de la tabla

if par_nombrePais !="":
    dfDatos=dfDatos[dfDatos["country"].str.upper().str.contains(par_nombrePais.upper())]

if par_fertilidad>0:
    dfDatos=dfDatos[dfDatos["fertility"]>= par_fertilidad]

dfDatos=dfDatos[(dfDatos["lifeExpectancy"]>=par_rangoExpectativaVida[0]) & (dfDatos["lifeExpectancy"]<=par_rangoExpectativaVida[1])]

st.metric("Registros Totales", len (dfDatos))
st.dataframe(dfDatos, use_container_width=True)