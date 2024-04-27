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

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="wide", initial_sidebar_state="collapsed", menu_items=None)
#------------------------------------------------------------------------------------------------
#STYLE CSS
#with open('html/style.css') as f:
    #st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#HTML
#with open("html/index.html", "r") as file:
    #index = file.read()
    #st.markdown(index, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#CONTACT
#with open("html/contacts.html", "r") as file:
    #contacts = file.read()
    #st.markdown(contacts, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#contact()

st.markdown('<!DOCTYPE html>', unsafe_allow_html=True)
st.markdown('<html lang="en">', unsafe_allow_html=True)

st.markdown('<head>', unsafe_allow_html=True)
st.markdown('<meta charset="UTF-8">', unsafe_allow_html=True)
st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0">', unsafe_allow_html=True)
st.markdown('<title>Mobile App Screen</title>', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">', unsafe_allow_html=True)
st.markdown('<style>', unsafe_allow_html=True)
st.markdown('.menu { display: none; }', unsafe_allow_html=True)
st.markdown('.content { padding: 20px; }', unsafe_allow_html=True)
st.markdown('@media only screen and (min-width: 768px) { .navbar { background-color: #007bff; color: white; padding: 10px 0; } .nav-link { color: white !important; padding: 0 10px !important; } }', unsafe_allow_html=True)
st.markdown('@media only screen and (max-width: 767px) { .navbar { position: fixed; bottom: 0; width: 100%; background-color: #007bff; color: white; display: flex; justify-content: space-around; padding: 10px 0; } .nav-link { color: white !important; padding: 0 10px !important; } }', unsafe_allow_html=True)
st.markdown('</style>', unsafe_allow_html=True)
st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">', unsafe_allow_html=True)

st.markdown('</head>', unsafe_allow_html=True)

st.markdown('<body>', unsafe_allow_html=True)
st.markdown('<nav class="navbar">', unsafe_allow_html=True)
st.markdown('<a class="nav-link" href="#" onclick="showScreen(\'screen1\')">Home</a>', unsafe_allow_html=True)
st.markdown('<a class="nav-link" href="#" onclick="showScreen(\'screen2\')">About</a>', unsafe_allow_html=True)
st.markdown('<a class="nav-link" href="#" onclick="showScreen(\'screen3\')">Services</a>', unsafe_allow_html=True)
st.markdown('<a class="nav-link" href="#" onclick="showScreen(\'screen4\')">Contact</a>', unsafe_allow_html=True)
st.markdown('</nav>', unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="content" id="screen1">', unsafe_allow_html=True)
st.markdown('<h1>Title</h1>', unsafe_allow_html=True)
st.markdown('<p>This is the first paragraph on the home screen.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="content" id="screen2" style="display: none;">', unsafe_allow_html=True)
st.markdown('<h1>Tables</h1>', unsafe_allow_html=True)
st.markdown('<table class="table">', unsafe_allow_html=True)
st.markdown('<thead>', unsafe_allow_html=True)
st.markdown('<tr>', unsafe_allow_html=True)
st.markdown('<th>Heading 1</th>', unsafe_allow_html=True)
st.markdown('<th>Heading 2</th>', unsafe_allow_html=True)
st.markdown('</tr>', unsafe_allow_html=True)
st.markdown('</thead>', unsafe_allow_html=True)
st.markdown('<tbody>', unsafe_allow_html=True)
st.markdown('<tr>', unsafe_allow_html=True)
st.markdown('<td>Data 1</td>', unsafe_allow_html=True)
st.markdown('<td>Data 2</td>', unsafe_allow_html=True)
st.markdown('</tr>', unsafe_allow_html=True)
st.markdown('<tr>', unsafe_allow_html=True)
st.markdown('<td>Data 3</td>', unsafe_allow_html=True)
st.markdown('<td>Data 4</td>', unsafe_allow_html=True)
st.markdown('</tr>', unsafe_allow_html=True)
st.markdown('</tbody>', unsafe_allow_html=True)
st.markdown('</table>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="content" id="screen3" style="display: none;">', unsafe_allow_html=True)
st.markdown('<h1>Contact Page</h1>', unsafe_allow_html=True)
st.markdown('<p>Here you can place a contact form or contact information.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<script>', unsafe_allow_html=True)
st.markdown('function showScreen(screenId) { document.querySelectorAll(\'.content\').forEach(content => { content.style.display = \'none\'; }); document.getElementById(screenId).style.display = \'block\'; }', unsafe_allow_html=True)
st.markdown('</script>', unsafe_allow_html=True)

st.markdown('<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>', unsafe_allow_html=True)
st.markdown('<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>', unsafe_allow_html=True)
st.markdown('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>', unsafe_allow_html=True)
st.markdown('</body>', unsafe_allow_html=True)

st.markdown('</html>', unsafe_allow_html=True)
