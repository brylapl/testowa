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
from tab1 import tab1

st.write('APP')

from tab1 import show_tab1
from tab2 import show_tab2

# Tworzenie zakładek
tabs = st.radio("Wybierz zakładkę:", ["Tab1", "Tab2"])

if tabs == "Tab1":
    show_tab1()
elif tabs == "Tab2":
    show_tab2()
