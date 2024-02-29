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
try:
    c = conn.cursor()
    st.write('połączono') 
except:
    st.write('błąd') 
# Wykonanie zapytania SQL
btn = st.button('start')

if btn:
    # Pobranie unikalnych połączeń dwóch kolumn
    c.execute('SELECT DISTINCT KRAJ, LIGA FROM list_teams')
    rows = c.fetchall()
    unique_values = {}
    for row in data:
        country = row[0]
        city = row[1]
        
        if country not in unique_values:
            unique_values[country] = [city]
        else:
            unique_values[country].append(city)
            
          
    for country, cities in unique_values.items():
        st.write(country)
    for city in cities:
        st.write(f"- {city}")
    #st.markdown(html_list,unsafe_allow_html=True)

# Zapisanie do pliku html
#with open("lista.html", "w") as file:
    #file.write(html_list)

# Zakończenie połączenia
#conn.close()
