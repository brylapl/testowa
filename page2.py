import streamlit as st

st.title("Strona 2")

# Opcjonalnie link do powrotu do strony głównej
if st.button("Powrót do głównej"):
    st.experimental_rerun()  # Odświeżenie widoku
    st.session_state.page = 'app'
