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
#-------------------------------------------------------------------------------------------
from session_state import get

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
st.header('baza danych')

session_state = get(user_id=None)

if session_state.user_id is None:
    login = st.text_input('Login')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        # Tutaj dodaj kod weryfikujący poprawność loginu i hasła
        # np. pobranie danych z bazy danych i porównanie z wpisanymi wartościami

        # Imitacja poprawności hasła (dla potrzeb przykładu)
        if login == 'admin' and password == 'admin':
            session_state.user_id = 1
        elif login == 'user' and password == 'user':
            session_state.user_id = 2
        else:
            st.error('Nieprawidłowy login lub hasło!')
else:
    if session_state.user_id == 1:
        st.write('Witaj, administrator!') # Strona administracyjna
    else:
        st.write('Witaj, zwykły użytkowniku!') # Strona startowa dla zwykłych użytkowników
