from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import streamlit as st 

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get('http://onet.pl')
st.write(driver.title)
driver.quit()
