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

# # 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
    
# selected5 = option_menu(None, ["Home", "Calculator", "Contact", 'About'],
#                         icons=['bi-house-door-fill', 'bi-file-bar-graph-fill', "bi-envelope-at-fill", 'bi-info-square-fill'],
#                         on_change=on_change, key='menu_5', orientation="horizontal")

# if selected5 == "Home":
#     st.write("You selected the Home page")    
# elif selected5 == "Upload":
#     st.write("You selected the Upload page")
# elif selected5 == "Contact":
#     with open("contact.html", "r") as file:
#         con = file.read()
#         st.markdown(con, unsafe_allow_html=True)
#     contact()
# elif selected5 == "About":
#     with open("about.html", "r") as file:
#         about_content = file.read()
#         st.markdown(about_content, unsafe_allow_html=True)


# Funkcja do tworzenia ikon z tekstem
def icon_text(icon, text):
    return f'<div style="display: flex; justify-content: center; align-items: center;"><div style="padding: 5px;"><i class="{icon}" style="font-size: 24px;"></i></div><div>{text}</div></div>'

# Ustawienia CSS dla menu bar
st.markdown("""
<style>
.menu-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    background-color: #f0f0f0;
    height: 60px;
    box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.1);
}
.menu-item {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 1;
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.menu-item:hover {
    background-color: #e0e0e0;
}
</style>
""", unsafe_allow_html=True)

# Ikony do wyświetlenia w menu bar
icons = ["fas fa-home", "fas fa-search", "far fa-user"]

# Teksty odpowiadające ikonom
texts = ["Home", "Search", "Profile"]

# Menu bar
st.markdown('<div class="menu-bar">', unsafe_allow_html=True)
for i in range(len(icons)):
    st.markdown('<div class="menu-bar"> <button class="menu-btn">Icon 1 - Text 1</button> <button class="menu-btn">Icon 2 - Text 2</button> <button class="menu-btn">Icon 3 - Text 3</button> </div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
