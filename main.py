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

#------------------------ TABELA NA KURSY
from weasyprint import HTML

# Tworzenie formularza w aplikacji Streamlit
st.markdown("# Wprowadź dane:")
name = st.text_input("Wprowadź swoje imię")
age = st.text_input("Wprowadź swój wiek")

# Utworzenie zawartości do zapisania do pliku PDF
html = f"<h1>{name}</h1>"
html += f"<p>Wiek: {age}</p>"

# Zapisanie zawartości do pliku PDF
pdf_file = f"{name}_info.pdf"
HTML(string=html).write_pdf(pdf_file)

# Wyświetlenie linku do pobrania pliku PDF
st.markdown(f"[Pobierz plik PDF z informacjami]({pdf_file})")









