import streamlit as st
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

driver = uc.Chrome(headless=True,use_subprocess=False)
url = st.text_input('Wpisz adres') 

if url != '' and st.button('Uruchom'):
    driver.get(url)
    st.write(driver.title)
