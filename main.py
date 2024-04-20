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
import mysql.connector
from contact import contact
#-------------------------------------------------------------------------------------------
from streamlit_option_menu import option_menu
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
#------------------------------------------------------------------------------------------------
#STYLE CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    
selected5 = option_menu(None, ["Home", "Calculator", "Contact", 'About'],
                        icons=['bi-house-door-fill', 'bi-file-bar-graph-fill', "bi-envelope-at-fill", 'bi-info-square-fill'],
                        on_change=on_change, key='menu_5', orientation="horizontal")

if selected5 == "Home":
    st.write("You selected the Home page")    
elif selected5 == "Upload":
    st.write("You selected the Upload page")
elif selected5 == "Contact":
    with open("contact.html", "r") as file:
        con = file.read()
        st.markdown(con, unsafe_allow_html=True)
elif selected5 == "About":
    with open("about.html", "r") as file:
        about_content = file.read()
        st.markdown(about_content, unsafe_allow_html=True)
