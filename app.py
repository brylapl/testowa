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

conn = sqlite3.connect('soccer.db')
c = conn.cursor()
if st.button('Start'):
  for row in c.execute(f'SELECT * FROM flagi'):
    st.write(row)
