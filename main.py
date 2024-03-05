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
import smtplib
import time

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
st.header('baza danych')

l = st.secrets["login"]
p = st.secrets["pass"]

# Funkcja do wysyłania maila
def send_email():
    st.text("Sending email...")
    server = smtplib.SMTP('smtp.wp.pl',587)
    server.starttls()
    server.login(l, p)
    server.sendmail("srspl@wp.pl", "srspl@wp.pl", "This is a test email")
    server.quit()
    st.text("Email sent successfully")

if st.button('start'):
    send_email() 
st.write('Dane ')
