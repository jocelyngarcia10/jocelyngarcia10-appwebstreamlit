import re
import streamlit as st
import time

def is_valid_email(email):
    email_patter = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_patter,email) is not None

@st.dialog("contacto")
def contact_form():
    with st.form("contact_form"):
        email= st.text_input("Correo Electronico",placeholder="email@mail.com")
        name = st.text_input("Nombre:", placeholder="Escriba su nombre")
        message = st.text_area("MEnsaje:")
        submit_button = st.form_submit_button("Enviar")

    if submit_button:  
        if not name:  
            st.error("Por favor escriba su nombre.")
            st.stop() 
            if not is_valid_email():
                st.error("Por favor su dirección decorreo electronico no es correcta")
                st.stop()
        if not email:
            st.error("Por favor escriba su dirección de correo electronico ")    
        st.stop()
    if not message:
        st.error("Por favor escrina un mensaje")    
        st.stop()
    if submit_button:
        st.success("se envio satisfactoriamente")    
        time.sleep(2)
        st.rerun()

