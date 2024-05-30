from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get('http://selenium.dev')
st.write(driver.title)
driver.quit()
