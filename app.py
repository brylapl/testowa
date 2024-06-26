from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument("--headless=new")
options.add_argument('--verbose')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--window-size=1920x1080")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
driver = webdriver.Chrome(options=options)
url = st.text_input("podaj adres strony")

start = st.button('START')


if start:
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    driver.maximize_window()
    st.write(driver.title)
    #Znajdz najblizszy mecz
    upcoming_match = driver.find_element(By.CSS_SELECTOR, '#desktopDiv > div.container.p-1 > div:nth-child(5) > div:nth-child(1) > div > div > div > a')
    st.write(upcoming_match.text)
    upcoming_match.click()
    
    driver.switch_to.window(driver.window_handles[1])
    driver.save_screenshot("image.png")
    st.image("image.png")
    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@id="sidebar-scroll"]/div/div[1]/ul/li[4]/button)[1]')))
    
    if dropdown.text.strip() == 'Last 5 games':
        dropdown.click()
        sleep(0.5)
        all_games = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="dropdown-menu show"]/a[last()]')))
        all_games.click()
    else:
        st.write('Nie otwarto wszystkich meczów')
    sleep(1)
    
    try:
        home_all_games = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="dropdown-menu"])[1]/../preceding-sibling::li[3]/button')))
        sleep(1)
        home_all_games.click()
    except:
        pass
    
    try:
        away_all_games = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="dropdown-menu"])[1]/../following-sibling::li[1]/button')))
        sleep(1)
        away_all_games.click()
    except:
        pass
    
    sleep(1)
    
    #MAKEYOURSTATS SCORED , CONCEDED, xG I xGA
    
    #HOME NAME
    home_name_makestats = driver.find_element(By.CSS_SELECTOR,'#game-top > div > div.col-md-4.align-self-cente.p-0 > p.font-weight-bolder.text-center.mt-1.d-none.d-xl-block.text-dark').text
    
    #HOME SCORED AND CONCEDED
    scored_home_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Avg. goals scored"]/../preceding-sibling::div//span').text 
    scored_home_makestats = float(scored_home_makestats)
    HOME_POINT.append(scored_home_makestats)
    conceded_home_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Avg. goals conceded"]/../preceding-sibling::div//span').text 
    conceded_home_makestats = float(conceded_home_makestats)
    
    
    try:
        #HOME xG AND xGA
        xg_home_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals (xG)"]/../preceding-sibling::div//span').text 
        xg_home_makestats = float(xg_home_makestats)
        HOME_POINT.append(xg_home_makestats)
        xga_home_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals against (xGA)"]/../preceding-sibling::div//span').text 
        xga_home_makestats = float(xga_home_makestats)
       
    except:
        pass
    #--------------------------------------------------------
    #--------------------------------------------------------
    #--------------------------------------------------------
    
    #AWAY NAME
    away_name_makestats = driver.find_element(By.CSS_SELECTOR,'#game-top > div > div.col-md-4.align-self-center.pointer > p.font-weight-bolder.text-center.mt-1.d-none.d-xl-block.text-dark').text
    
    #AWAY SCORED AND CONCEDED
    scored_away_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Avg. goals scored"]/../following-sibling::div//span').text 
    scored_away_makestats = float(scored_away_makestats)
    AWAY_POINT.append(scored_away_makestats)
    conceded_away_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Avg. goals conceded"]/../following-sibling::div//span').text
    conceded_away_makestats = float(conceded_away_makestats)
   
    
    try:
        #AWAY xG AND xGA
        xg_away_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals (xG)"]/../following-sibling::div//span').text
        xg_away_makestats = float(xg_away_makestats)
        AWAY_POINT.append(xg_away_makestats)	
        xga_away_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals against (xGA)"]/../following-sibling::div//span').text
        xga_away_makestats = float(xga_away_makestats)
        
    except:
        pass
    st.write(home_name_makestats,away_name_makestats,scored_home_makestats,scored_away_makestats)

driver.quit()
