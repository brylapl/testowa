import streamlit as st


def contact():
    # Formularz zgłaszania błędów i propozycji zmian
    st.title("Formularz zgłaszania błędów i propozycji zmian")
    
    category = st.selectbox("Wybierz kategorię zgłoszenia:", ["Error", "New"])
    
    message = st.text_area("Wiadomość")
    email = st.text_input("Email kontaktowy")
    
    if st.button("Wyślij"):
        st.success("Zgłoszenie zostało wysłane pomyślnie!")
