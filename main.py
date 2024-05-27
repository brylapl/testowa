import undetected_chromedriver as uc
import streamlit as st
import streamlit.components.v1 as components
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Define a custom user agent
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
 
# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument(f"user-agent={my_user_agent}")
 
# Initialize Chrome WebDriver with the specified options
driver = uc.Chrome(options=options)
 
# Make a request to your target website.
driver.get("https://www.nowsecure.nl/")
st.write(driver.title)
# Close the driver
driver.quit()
 
