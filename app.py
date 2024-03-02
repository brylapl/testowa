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

conn = sqlite3.connect('soccer.db')
c = conn.cursor()
name = st.text_input('Wybierz kraj')
wzor = 'https://flagcdn.com/16x12/'
if name != '':
  if st.button('Start'):
    for row in c.execute(f'''SELECT url FROM flagi 
                             WHERE src = "{name}" '''):
                               st.markdown(f'<img src="{wzor}url.png"')
