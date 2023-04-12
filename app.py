from pathlib import Path
import streamlit as st
from PIL import Image
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


URL = "https://www.onet.pl"

st.title("Test Selenium")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install())
    options=firefoxOptions,
    service=service,
)



driver.get(URL)

title = driver.title
st.write(title)
driver.quit()
