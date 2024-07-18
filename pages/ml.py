import streamlit as st
import streamlit.components.v1 as components

st.title('STRONA ZAWIERA ML')

components.iframe("https://www.flashscore.pl", height=500, scrolling=True)

components.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
