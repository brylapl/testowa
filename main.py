import streamlit as st
import undetected_chromedriver as uc
driver = uc.Chrome(headless=True,use_subprocess=False)
url = st.text_input('Wpisz adres') 

if url != '' and st.button('Uruchom'):
    driver.get(url)
    st.write(driver.title)
