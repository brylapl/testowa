from bs4 import BeautifulSoup
import requests
import lxml 
from time import sleep
import time
from datetime import datetime
from datetime import timedelta
import sqlite3
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
from contact import contact
#-------------------------------------------------------------------------------------------
from streamlit_option_menu import option_menu
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
#------------------------------------------------------------------------------------------------
#STYLE CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------

# # 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
    
# selected5 = option_menu(None, ["Home", "Calculator", "Contact", 'About'],
#                         icons=['bi-house-door-fill', 'bi-file-bar-graph-fill', "bi-envelope-at-fill", 'bi-info-square-fill'],
#                         on_change=on_change, key='menu_5', orientation="horizontal")

# if selected5 == "Home":
#     st.write("You selected the Home page")    
# elif selected5 == "Upload":
#     st.write("You selected the Upload page")
# elif selected5 == "Contact":
#     with open("contact.html", "r") as file:
#         con = file.read()
#         st.markdown(con, unsafe_allow_html=True)
#     contact()
# elif selected5 == "About":
#     with open("about.html", "r") as file:
#         about_content = file.read()
#         st.markdown(about_content, unsafe_allow_html=True)

def btn():
    btn = st.button('Uruchom')
st.markdown('''
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Strona główna</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<div class="container-fluid vh-100" style="background-image: url('https://www.cio.com/wp-content/uploads/2023/05/statistics-stats-big-data-analytics-100613892-orig-4.jpg'); background-size: cover; background-position: center;">
<h1>Element zajmujący 100% wysokości ekranu</h1>
<p>Tu znajduje się treść pierwszego elementu strony</p>
</div>

<div class="container">
<h2>Treść dopiero po przewinięciu w dół</h2>
<p>Tu znajduje się kolejna treść strony po przewinięciu</p>
</div>

<!-- Skrypty Bootstrap 5 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''', unsafe_allow_html=True)
btn()
