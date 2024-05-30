from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import streamlit as st

st.text('Test')

browser = webdriver.Firefox()

browser.get('http://www.onet.pl')
st.title(browser.title)
browser.quit()
