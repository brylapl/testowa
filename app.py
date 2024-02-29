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
c = conn.cursor()

# Wykonanie zapytania SQL
c.execute("SELECT DISTINCT KRAJ, LIGA FROM list_teams")
rows = c.fetchall()

# Tworzenie listy zagnieżdżonej
html_list = "<ul>"
for row in rows:
    html_list += "<li>" + row[0] + "<ul><li>" + row[1] + "</li></ul></li>"
html_list += "</ul>"

st.markdown('html_list',unsafe_allow_html=True)
# Zapisanie do pliku html
#with open("lista.html", "w") as file:
    #file.write(html_list)

# Zakończenie połączenia
conn.close()
