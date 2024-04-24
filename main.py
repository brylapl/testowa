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
with open('html/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#HTML
# with open("html/index.html", "r") as file:
#     index = file.read()
#     st.markdown(index, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------


st.title("Markdown bug")
st.caption('Output')

def tweet_button(tag: str, 
                 link: str, 
                text: str, 
                user: str):
  tweet = f"""
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
  <script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
  <a href="https://x.com/intent/tweet?url={link}&text={text}&via={user}&hashtags={tag}">
  <button class="ui twitter button large ui button">
   <i class="twitter icon"></i>
    Tweet
  </button></a>
    """
st.markdown(tweet, unsafe_allow_html=True)

st.write("")

tweet_button(tag='streamlit, share', 
             link='https://30days.streamlit.app/', 
             text='Streamlit share button', 
             user='streamlit')

st.write("")
st.write('📌 NOTE: This button only works if you have a valid Twitter account.')




