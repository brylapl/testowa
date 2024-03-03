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
from tabele import sklady_wyjsciowe

st.write('APP')

lista1 = [1,2,3,4,5]
lista2 = [10,11,12]
flagi_home = ['f1','f2','f3','f4','f5']
flagi_away = ['f10','f11','f12']
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.write('STRONA 1')
   
with tab2:
    st.header('Jakias druga')

with tab3:
    st.write('WYWOŁANA FUNKCJĄ ZEWNĘTRZNĄ')
    
    sklady_wyjsciowe(lista1,lista2,flagi_home,flagi_away)
    

