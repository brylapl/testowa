from bs4 import BeautifulSoup
import requests
import lxml
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

st.write('APP')
st.header('Tytul')

import streamlit as st
import sqlite3
from datetime import datetime

# Tworzenie bazy danych SQLite
conn = sqlite3.connect('soccer.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS errors 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              error_text TEXT, 
              error_date TEXT)''')

# Formularz zgłaszania błędów
st.write("# Formularz zgłaszania błędów")

error_text = st.text_area("Opisz znaleziony błąd:")
if st.button("Zgłoś"):
    error_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO errors (error_text, error_date) VALUES (?, ?)", (error_text, error_date))
    conn.commit()
    st.success("Błąd został zgłoszony pomyślnie!")

# Wyświetlanie błędów z bazy danych
st.write("# Lista zgłoszonych błędów")
if st.button("Pokaż błędy"):
    errors = c.execute("SELECT * FROM errors").fetchall()
    for error in errors:
        st.write(f"ID: {error[0]}, Opis błędu: {error[1]}, Data zgłoszenia: {error[2]}")

conn.close()

