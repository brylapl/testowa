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
import schedule
import time

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
st.header('baza danych')



# Funkcja do wysyłania maila
def send_email():
    st.text("Sending email...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", "recipient_email@gmail.com", "This is a test email")
    server.quit()
    st.text("Email sent successfully")

# Funkcja do planowania wysyłania maila o ustalonej godzinie
def schedule_email():
    schedule.every().day.at("12:00").do(send_email)  # Ustawienie godziny wysyłki maila
    while True:
        schedule.run_pending()
        time.sleep(1)

# Wywołanie funkcji planowania wysyłania maila
schedule_email()


st.write("DB username:", st.secrets["LOGIN"])
st.write("DB password:", st.secrets["PASSWORD"])
