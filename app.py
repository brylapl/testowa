from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument("--headless=new")
options.add_argument('--verbose')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920x1080")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
driver = webdriver.Chrome(options=options)

# url = st.text_input("podaj adres strony")
# start = st.button('START')
# if start:
#     driver.get(url)
#     driver.quit()



st.page_link("app.py", label="Home", icon="🏠")
st.page_link("/pages/contact.py", label="Page 1", icon="1️⃣")

if st.button("Home"):
    st.switch_page("app.py")
if st.button("Page 1"):
    st.switch_page("pages/contact.py")
