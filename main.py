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
from time import sleep
#-------------------------------------------------------------------------------------------

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
st.header('baza danych')

try:
    conn = sqlite3.connect('soccer.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS errors 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   error_text TEXT, 
                   error_date TEXT)''')
    st.write('utworzono tabele errors')
    autocommit = conn.isolation_level is None
    if autocommit:
        st.write("Autocommit jest włączony")
    else:
        st.write("Autocommit jest wyłączony")
except:
    st.write('nie utworzono errors')

conn.set_isolation_level(None)
autocommit = conn.isolation_level is None
if autocommit:
    st.write("Autocommit jest włączony")
else:
    st.write("Autocommit jest wyłączony")
    
        
st.write("# Formularz zgłaszania błędów")
error_text = st.text_area("Opisz znaleziony błąd:")
if st.button("Zgłoś"):
    error_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO errors (error_text, error_date) VALUES (?, ?)", (error_text, error_date))
    try:
        conn.commit()
        st.markdown('''<div class="alert alert-success text-center" role="alert">Błąd został zgłoszony pomyślnie!</div>''', unsafe_allow_html=True)
        st.write('commit wykonany') 
    except Exception as e:
        st.write(f"Wystąpił błąd: {str(e)}")
