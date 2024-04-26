import streamlit as st

def contact():
    kategoria = st.selectbox('Kategoria', ['Błąd','Nowe funkcje','Inne'],help="Wybierz kategorię wiadomości w jakiej chcesz się skontaktować.")
    wiadomosc = st.text_area('Wiadomość')
    email = st.text_input('Email (opcjonalnie)', help="Podaj swój e-mail jeżeli Twoja wiadomość wymaga odpowiedzi.")
    
    if st.button('Wyślij'):
        st.success('Wiadomość została wysłana.')
