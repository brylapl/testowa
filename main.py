from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("no-sandbox")
options.add_argument("headless")
options.add_argument("start-maximized")
options.add_argument("window-size=1900,1080"); 
driver = webdriver.Chrome(options=options)

driver.get("https://www.onet.pl")
html = driver.page_source
st.write(html)
