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

#POŁĄCZENIE Z BAZĄ DANYCH
# Połączenie z bazą danych SQLite3
conn = sqlite3.connect('soccer.db')
c = conn.cursor()

# Utworzenie tabeli errors, jeśli nie istnieje
c.execute('''CREATE TABLE IF NOT EXISTS errors
             (id INTEGER PRIMARY KEY AUTOINCREMENT, error_description TEXT)''')

# Dodanie formularza zgłaszania błędów
st.title('Formularz zgłaszania błędów')

error_description = st.text_area('Opis błędu')

if st.button('Zgłoś błąd') and error_description:
    c.execute(f"INSERT INTO errors (error_description) VALUES ('{error_description}')")
    conn.commit()
    st.success('Błąd został pomyślnie zgłoszony!')

# Dodanie przycisku do wyświetlania błędów
if st.button('Wyświetl zgłoszone błędy'):
    errors = c.execute('SELECT * FROM errors').fetchall()
    if errors:
        st.write('Zgłoszone błędy:')
        for error in errors:
            st.write(f'- {error[1]}')
    else:
        st.write('Brak zgłoszonych błędów')

# Zamykanie połączenia z bazą danych
conn.close()
