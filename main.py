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

# Usuwanie całego domyślnego kodu HTML i CSS
st.markdown("""<style>
.st-dm{
    display: none;
}
.root {
display: none;
}
.menu {
    display: none;
    }
.content {
    padding: 20px;
}
@media only screen and (min-width: 768px) {
.navbar {
    background-color: #007bff;
    color: white;
    padding: 10px 0;
}
.nav-link {
    color: white !important;
    padding: 0 10px !important;
}
}
    
@media only screen and (max-width: 767px) { 
.navbar { 
position: fixed; 
bottom: 0; 
width: 100%; 
background-color: #007bff; 
color: white; 
display: flex; 
justify-content: space-around; 
padding: 10px 0; 
} 
.nav-link { 
color: white !important; 
padding: 0 10px !important; 
} 
}
</style>""", unsafe_allow_html=True)

# Dodawanie własnego kodu HTML
st.markdown("""<h1>Witaj, to jest mój czysty dokument HTML!</h1>
<p>Tutaj możesz dodać swoje własne elementy HTML i stylować je według własnych preferencji.</p>""", unsafe_allow_html=True)
