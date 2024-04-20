import streamlit as st

def contact():
    st.title('Formularz kontaktowy')
    wiadomosc = st.text_area('Wiadomość')
    email = st.text_input('Email (opcjonalnie)')
    kategoria = st.selectbox('Kategoria', ['błąd', 'new'])
    
    if st.button('Wyślij'):
        st.success('Wiadomość została wysłana.')
