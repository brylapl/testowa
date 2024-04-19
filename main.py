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
#-------------------------------------------------------------------------------------------
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
st.header('BAZA DANYCH')

try:
    conn = mysql.connector.connect( host=st.secrets["host"], user=st.secrets["user"], password=st.secrets["password"], database=st.secrets["database"] )
    st.write("Połączenie z bazą danych zostało nawiązane")
except:
    st.write(f"Błąd połączenia z bazą danych")

c = conn.cursor()

st.button("Start", type="primary")

