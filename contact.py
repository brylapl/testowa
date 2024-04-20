import streamlit as st

def contact():
    st.markdown("<h1 style='text-align: center;'>Formularz kontaktowy</h1>", unsafe_allow_html=True)
    st.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"> ', unsafe_allow_html=True)
   
    with st.form(key='contact_form', clear_on_submit=True):
        st.text_input('Imię', key='name')
        st.text_input('Email', key='email')
        st.text_area('Wiadomość', key='message', height=200)
    st.form_submit_button('Wyślij', class_='btn btn-primary')
