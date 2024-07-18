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


def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

# Widgets shared by all the pages
st.sidebar.selectbox("Foo", ["A", "B", "C"], key="foo")
st.sidebar.checkbox("Bar", key="bar")

pg = st.navigation(st.Page(page1), st.Page(page2))
pg.run()
