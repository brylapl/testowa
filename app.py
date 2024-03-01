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
conn = sqlite3.connect('soccer.db')
c.execute('''CREATE TABLE IF NOT EXISTS errors (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT)''')
st.title('Formularz zgłaszania błędów')

error_description = st.text_area('Opis błędu')

if st.button('Zgłoś błąd'):
    c.execute('INSERT INTO errors (description) VALUES (?)', (error_description,)) 
    conn.commit() 
    st.success('Błąd został zgłoszony')

if st.button('Pokaż błędy'): 
    errors = c.execute('SELECT * FROM errors').fetchall() 
    errors_list = [error[1] for error in errors] 
    st.write('Błędy zgłoszone przez użytkowników:') 
    st.write(errors_list)

conn.close()
