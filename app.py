from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from flask import Flask, render_template
import streamlit.components.v1 as components

with open("html/test.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=2000)

# options = Options()
# options.add_argument("--headless=new")
# options.add_argument('--verbose')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument("--window-size=1920x1080")
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
# driver = webdriver.Chrome(options=options)

# url = st.text_input("podaj adres strony")
# start = st.button('START')
# if start:
#     driver.get(url)
#     driver.quit()


