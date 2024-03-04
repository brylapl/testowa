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
import funkcja
from io import BytesIO
#------------------------ TABELA NA KURSY
# Tworzenie tabeli HTML
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
table = '<table><tr><th>col1</th><th>col2</th></tr>'
for i in range(len(data['col1'])):
    table += f'<tr><td>{data["col1"][i]}</td><td>{data["col2"][i]}</td></tr>'
table += '</table>'
st.markdown(table, unsafe_allow_html=True)

# Input na hasło
password = st.text_input('Podaj hasło:', type='password')

# Przycisk do pobierania PDF
if st.button('Pobierz PDF'):
    if password == 'testowe':
        # Pobieranie pliku PDF
        st.write('Plik PDF został wygenerowany.')
        st.markdown(f'<a href="data:application/octet-stream;base64,{pdf_io.getvalue().decode("utf-8")}" download="raport.pdf">Pobierz PDF</a>', unsafe_allow_html=True)
    else:
        st.warning('Podane hasło jest nieprawidłowe.')









