import json
import requests
import streamlit as  st
from streamlit_lottie import st_lottie

#https://lottie.host/0040ee1a-8bce-47fc-bb62-e94229569496/adkUw60jds.json

def get(path:str):
    with open(path, "r") as p:
        return json.load(p)
#funcion lottie URL
def get_url(url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#Inicio de pagina
with st.container():
    st.subheader("Bienvenidos, Somos SOFTIA🙋‍♀️")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de las tenologías y la innovación, especialización en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos. "
    )
    st.write("[Saber más>](https://streamlit.io/)"
    )

#Sobre nosostros
with st.container():
    st.write("---")

    texto_columna, imagen_columna = st.columns((1,2))
    with texto_columna:
        st.subheader("Sobre nosotros 🧐💗")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.

Seguramente te vamos a poder ayudar si:

-Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido

para tu negocio

No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos

-Quieres mejorar la experiencia de tus clientes

Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y boligrafo

***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***

            """
    )
    with imagen_columna:
        st.image("img/sobrenosotros.png")
      
        
    

#Servicios

with st.container():
    st.write("---")
    st.header("Servicios 👩‍💻👨‍💻")


    texto_columna, imagen_columna = st.columns((1,2))


with texto_columna:
    st.subheader("Diseño de aplicaciones")

    st.write(
        """
        Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que 
        trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarias
        """
    )
    st.write("[Ver servicios >](https://streamlit.io/)")
   
   
    with imagen_columna: 
     path = get("animaciones/Ani.json")
     st_lottie(path)

    #st.image("img/image.png")

#Contactos
st.subheader("Contactos")

form = st.form(key="home", clear_on_submit=True)

with form:
    input_nombre = st.text_input("Nombre:", placeholder="Escriba su nombre")
    input_email = st.text_input("Correo electónico:", placeholder="Escriba su E-mail")
    input_area = st.text_area("Comentario")
    button_submit = form.form_submit_button("Enviar")

    #footer
    with st.container():
        p1, p2, p3 = st.columns((3))
        with p1:
            st.subheader("Contactos:")
            st.write("***Dirección:*** Juigalpa, Chontales-Nicaragua")
            st.write("***Teléfono:*** +(505) 0000-0000")
        with p2:
            st.subheader("Servicios") 
            st.write("Automatización de progresos") 
            st.write("Visualizaión de datos")

        with p3:
            st.subheader("Redes Sociales")
            st.markdown("[YOUTUBE](https://www.youtube.com)")
            st.markdown("[Facebook](https://www.youtube.com)")   
            st.markdown("[Instagram](https://www.youtube.com)")   
