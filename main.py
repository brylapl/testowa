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

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="wide", initial_sidebar_state="collapsed", menu_items=None)
#------------------------------------------------------------------------------------------------
#STYLE CSS
#with open('html/style.css') as f:
    #st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#HTML
#with open("html/index.html", "r") as file:
    #index = file.read()
    #st.markdown(index, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#CONTACT
#with open("html/contacts.html", "r") as file:
    #contacts = file.read()
    #st.markdown(contacts, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#contact()
import streamlit as st

# Ustawienie szerokości menu dolnego
st.markdown(
    """
    <style>
    .st-bm {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-around;
        padding: 8px 0;
        background-color: #f7f7f7;
        border-top: 1px solid #ccc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Elementy menu dolnego
st.markdown(
    """
    <div class="st-bm">
        <div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Android_O_Preview_Logo.png/400px-Android_O_Preview_Logo.png" style="height: 24px;">
            <p>Strona główna</p>
        </div>
        <div>
            <img src="https://image.flaticon.com/icons/png/128/61/61848.png" style="height: 24px;">
            <p>Ustawienia</p>
        </div>
        <div>
            <img src="https://cdn4.iconfinder.com/data/icons/basic-ui-elements-coloricon/512/09_chat-128.png" style="height: 24px;">
            <p>Wiadomości</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
