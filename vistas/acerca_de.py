import streamlit as st 
from forms.contacto import contact_form

@st.dialog("contacto")
def ver_form_contacto():
    contact_form()


c1,c2 = st.columns (2, gap="small", vertical_alignment="center")

with c1:
    st.image("img/yo.png", width=230)
with c2:
    st.title ("Tecnologia para el mundo")
    st.write (
        "La tecnología es la aplicación de conocimientos científicos y técnicas productivas para crear herramientas, materiales y nuevas formas de comprender la realidad."
    )    
    if st.button("contacto"):
       contact_form()

st.subheader("Experiencias y Calificaciones", anchor=False)
st.write(
    """
    - 7 años de experiencia extrayendo información util a partir de datos.
    """
)

st.subheader("Habilidades", anchor=False)
st.write(
    """
    - Programción: Python (scikin-learn, pandas), SQL, VBA
     """
             
        )