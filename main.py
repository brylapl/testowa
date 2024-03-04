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
from time import sleep
#-------------------------------------------------------------------------------------------
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
import xgboost as xgb
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import metrics
from xgboost.core import Objective 
#-------------------------------------------------------------------------------------------
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Obliczanie kursów', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

#----------------------------------------
#TABELA DLA DANYCH O RÓZNEJ DŁUGOŚCI - KONTUZJE
#----------------------------------------

def tabela_kontuzje_rezerwowi(list1, list2,flagi_home,flagi_away,tytul,power=False):
    max_len = max(len(list1), len(list2))
    min_len = min(len(list1), len(list2))

    # dodanie pustych wartości do krótszej listy
    if len(list1) < max_len:
        list1 += [''] * (max_len - min_len)
        flagi_home += [''] * (max_len - min_len)


    elif len(list2) < max_len:
        list2 += [''] * (max_len - min_len)
        flagi_away += [''] * (max_len - min_len)


    # tworzenie tabeli HTML
    html = "<div class='container mw-100'>\n"
    html += "<table class='table table-responsive table-striped text-center table-dark table-sm'>\n"
    html += f"<tr><th class='fw-bold' colspan='4'>{tytul}</th></tr>"
    html += "<tr>\n"
    html += f"<th class='bg-dark text-white fw-bold' colspan='2'>{soccerrating_home_name}</th>\n"
    html += f"<th class='bg-dark text-white fw-bold' colspan='2'>{soccerrating_away_name}</th>\n"
    html += "</tr>\n"
    if power:
        html += "<tr>\n"
        html += f"<th class='bg-dark text-white fw-bold' colspan='2'>{stats_mg[0]}</th>\n"
        html += f"<th class='bg-dark text-white fw-bold' colspan='2'>{stats_mg[1]}</th>\n"
        html += "</tr>\n"
    for i in range(max_len):
        # flaga = flagi_home[i].split('/')[-1]
        # flaga = flaga.split('.')[0]
        # flaga = f'/content/{flaga}.svg'
        html += "<tr>\n"
        html += f"<td><img src='{flagi_home[i]}' alt=''</img></td><td>{list1[i]}</td>\n"

        html += f"<td><img src='{flagi_away[i]}' alt=''</img><td>{list2[i]}</td>\n"
        html += "</tr>\n"

    html += "</table>\n"
    html += "</div>"

    return html

#----------------------------------------
#TABELA DLA DANYCH O STAŁEJ DŁUGOŚCI WYJŚCIOWE SKŁADY
#----------------------------------------
def tabela_sklad_wyjsciowy(list1, list2):
    # Sprawdzenie czy obie listy zawierają po 11 elementów
    if len(list1) != 11 or len(list2) != 11:
        return "Błędne dane. Obie listy muszą zawierać po 11 elementów."

    # Rozpoczęcie tworzenia tabeli w HTML
    table_html = "<div class='container'>\n"
    table_html += "<table class='table'>\n"
    table_html += f"<tr><th colspan='2'>Składy wyjściowe</th></tr>"
    # Dodanie nagłówka tabeli
    
    # Dodanie nagłówków tabeli
    table_html += "<tr>"
    for col in stats_mg:
        table_html += "<th>{}</th>".format(col)
    table_html += "</tr>\n"

    # Dodanie zawartości tabeli na podstawie elementów z listy 1 i listy 2
    for i in range(11):
        table_html += "<tr>\n"
        table_html += f"<td><img src='{list1[i][:42]}' align='left' style='vertical-align:middle;margin:0px 0px 0px 80px'></img> {list1[i][42:]}</td>\n"
        table_html += f"<td><img src='{list2[i][:42]}' align='left' style='vertical-align:middle;margin:0px 0px 0px 80px'></img> {list2[i][42:]}</td>\n"
        table_html += "</tr>\n"

    # Zamknięcie tabeli w HTML
    table_html += "</table>\n"
    table_html += "</div>"

    # Zwrócenie wynikowej tabeli w HTML
    return table_html

#-----—----------—------------------------------
#TABELA DO WYŚWIETLENIA KURSÓW 
#-----------------------------------------------

def tytul(name):
	th = f'''<tr>\n<th class='bg-dark text-white fw-bold h2' colspan="3">{name}</th>\n</tr>\n'''
	return th
	
def rodzaj(*args):
            th = f'''<tr>\n<th class='bg-dark text-white fw-bold'>{args[0]}</th>\n<th class='bg-dark text-white fw-bold'>{args[1]}</th>\n<th class='bg-dark text-white fw-bold'>{args[2]}</th>\n</tr>\n'''
            return th

def dane(*kurs):
	for i in range(len(kurs)):
		       t = f'''<tr>\n<td>{kurs[0][0]}</td>\n<td class='bg-dark text-white fw-bold'>{kurs[0][1]}</td>\n<td>{kurs[0][2]}</td>\n</tr>\n'''
		     
	return t
		      
		       

def tabela_kursy():
	t = '<div class="container">\n'
	t += '<table class="table table-striped text-center table-dark">\n'
	t += '''<tr>\n<th class='bg-dark text-white fw-bold' colspan="3">Oczekiwane kursy</th>\n</tr>\n'''
	t += tytul('Regulaminowy czas')
	t += rodzaj('1','X','2')
	t += dane(win)
	t += tytul('Podwójna szansa')
	t += rodzaj('1X','12','X2')
	t += dane(dc)
	t += tytul('Gole')
	t += rodzaj('Over','Linia','Under')
	t += dane(gole0)
	t += dane(gole1)
	t += dane(gole2)
	t += dane(gole3)
	t += dane(gole4)
	t += tytul('DNB')
	t += rodzaj('Home','','Away')
	t += dane(dnb)
	t += tytul('Obie strzelą')
	t += rodzaj('Tak','','Nie')
	t += dane(bts)
	t += tytul('Gole gospodarzy')
	t += rodzaj('Over','','Under')
	t += dane(home0)
	t += dane(home1)
	t += tytul('Gole gości')
	t += rodzaj('Over','','Under')
	t += dane(away0)
	t += dane(away1)
	t += '</div>'
	return t

#--------------------------------------------------------------------------------------------------
# TABELA DO WYSWIETLENIA STRZELONE/STRACONE

def tabela_wyswietl():
    
    t = '<table class="table text-center table-dark table-sm">\n'
    t += '<tr>\n'
    t += '''<th class="empty"></th>
            <th colspan=5>STRZELONE</th>
            <th colspan=4>STRACONE</th>
    '''
    t += '</tr>\n'
    t += '<tr>\n'
    t += '<th>Home</th>\n'
    
    for i in range(len(strzelone_home)):
        t += f'<td class="bg-success">{strzelone_home[i]}</td>\n'
    
    for i in range(len(stracone_home)):
        t += f'<td class="bg-danger">{stracone_home[i]}</td>\n'
    t += '</tr>\n'
    t += '<tr>\n'
    t += '<th>Away</th>\n'
    
    for i in range(len(strzelone_away)):
        t += f'<td class="bg-success">{strzelone_away[i]}</td>\n'
    for i in range(len(stracone_away)):
        t += f'<td class="bg-danger">{stracone_away[i]}</td>\n'
    t += '</tr>\n'
    t += '</table>'
   
    
    return t


#--------------------------------------------------------------------------------------------------

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


st.markdown('''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Protest+Revolution&display=swap" rel="stylesheet">''',unsafe_allow_html=True)

st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    """,
    unsafe_allow_html=True
)
st.markdown('''<link rel="stylesheet" 
          href= 
"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css"> ''',unsafe_allow_html=True)	    


#POŁĄCZENIE Z BAZĄ DANYCH
conn = sqlite3.connect('soccer.db')
c = conn.cursor()
options = [row[0] for row in c.execute(f'SELECT ID FROM list_teams').fetchall()]
today_match = [row[0] for row in c.execute(f'SELECT Mecz FROM flashscore').fetchall()]
def web_driver():
        options = webdriver.ChromeOptions()
        options.add_argument('--verbose')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--enable-javascript")
        options.add_argument("--incognito")
        options.add_argument("--nogpu")
        options.add_argument("--window-size=1920x1080")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
        driver = webdriver.Chrome(options=options)
        return driver

driver = web_driver()
#------------------------------------------------------------------MENU BOCZNE------------------------------------------------------------------------------------------------
st.sidebar.header('Panel logowania')
def login():
	user = st.sidebar.text_input('Nazwa użytkownika')
	password = st.sidebar.text_input('Hasło', type='password')
	
	if st.sidebar.button('Zaloguj'):
		if user == 'admin' and password == 'admin123':
			st.sidebar.success('Zalogowano pomyślnie!')
		else:
			st.sidebar.error('Nieprawidłowa nazwa użytkownika lub hasło')
		
login()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ MENU GÓRNE <---------
menu0,menu1, menu2= st.tabs(["Home","Obsługiwane ligi","Zgłoś błąd"])

with menu0:
	st.markdown('''<h1 class='fw-bold text-center'>Obliczanie Kursów</h1>''',unsafe_allow_html=True)    
	team = st.multiselect('Wybierz drużynę', options,placeholder="Wybierz drużynę")
	if team != '':
		for t in team:
		    for row in c.execute(f'SELECT * FROM list_teams WHERE ID like "{t}"'):
		        st.markdown(f'''
		                    <div class="select_team">
		                        <h3 class="info text-white">Drużyna: 
		                        <span class="info text-white">{row[0]}</span>
		                        </h3>
		                        <h3 class="info text-white">Kraj: 
		                        <span class="info text-white">{row[1]}</span>
		                        </h3>
		                        <h3 class="info text-white">Liga: 
		                        <span class="info text-white">{row[2]}</span>
		                        </h3>
		                        </div>''',unsafe_allow_html=True)
		        APWIN = row[3]
		        MAKEYOURSTATS = row[4]
		        BESOCCER = row[5]
		        FOOTYSTATS = row[6]
		        SOCCERRATING = row[7]
		st.markdown('---')        
		start_button = st.button("Uruchom", type="primary")
		
		
		strzelone_home = []
		stracone_home = []
		
		strzelone_away = []
		stracone_away = []
		
		
		
		if start_button:
			HOME_POINT = []
			AWAY_POINT = []
			st.markdown('''<div class="alert alert-secondary text-center" role="alert">Analiza rozpoczęta... </div>''', unsafe_allow_html=True) 
			START = datetime.now() + timedelta(hours=1)
			#APWIN__________________________________________________________________________________________________________________________________________________________________________________	
			APWIN_status = False
			r = requests.get(APWIN,headers=headers)
			bs = BeautifulSoup(r.content,'lxml')
			upcoming_match_apwin = bs.select_one('#team-section > div > div.columns.is-centered.mt-5.is-align-items-center > div > div > div > div:nth-child(1) > div > div.buttons.is-centered.are-small.pb-5 > a.button.is-rounded.is-link.is-outlined.has-text-weight-semibold')['href']
			r = requests.get(f'{upcoming_match_apwin}',headers=headers)
			bs = BeautifulSoup(r.content,'lxml')
			
			home_name_apwin = bs.select_one('#prematch-section > div:nth-child(3) > div:nth-child(1) > div > div.p-4.p-3-mobile.has-text-centered > div > div.has-text-left > h3').text
			away_name_apwin = bs.select_one('#prematch-section > div:nth-child(3) > div:nth-child(2) > div > div.p-4.p-3-mobile.has-text-centered > div > div.has-text-left > h3').text
			
			
			st.markdown(f'<h2>{home_name_apwin} - {away_name_apwin}</h2>',unsafe_allow_html=True)
			
			#APWIN xG I xGA
			#HOME
			xg_home_apwin = bs.select_one('#prematch-section > div:nth-child(3) > div:nth-child(1) > div > div.p-4.p-3-mobile.has-text-centered > table:nth-child(3) > tbody > tr:nth-child(9) > td:nth-child(2)').text
			xg_home_apwin = float(xg_home_apwin)
			HOME_POINT.append(xg_home_apwin)
			
			xga_home_apwin = bs.select_one('#prematch-section > div:nth-child(3) > div:nth-child(1) > div > div.p-4.p-3-mobile.has-text-centered > table:nth-child(3) > tbody > tr:nth-child(10) > td:nth-child(2)').text
			xga_home_apwin = float(xga_home_apwin)
			AWAY_POINT.append(xga_home_apwin)
			
			#AWAY
			xg_away_apwin = bs.select_one('#prematch-section > div:nth-child(3) > div:nth-child(2) > div > div.p-4.p-3-mobile.has-text-centered > table:nth-child(3) > tbody > tr:nth-child(9) > td:nth-child(2)').text
			xg_away_apwin = float(xg_away_apwin)
			AWAY_POINT.append(xg_away_apwin)
			
			xga_away_apwin = bs.select_one('#prematch-section > div:nth-child(3) > div:nth-child(2) > div > div.p-4.p-3-mobile.has-text-centered > table:nth-child(3) > tbody > tr:nth-child(10) > td:nth-child(2)').text
			xga_away_apwin = float(xga_away_apwin)
			HOME_POINT.append(xga_away_apwin)
			
			if all([xg_home_apwin,xga_home_apwin,xg_away_apwin,xga_away_apwin]):
				APWIN_status = True
			#MAKEYOURSTATS____________________________________________________________________________________________________________________________________________________________________
			driver = web_driver()
			driver.get(MAKEYOURSTATS)
			
			#Znajdz najblizszy mecz
			upcoming_match_makeyourstats = driver.find_element(By.CSS_SELECTOR, '#desktopDiv > div.container.p-1 > div:nth-child(5) > div:nth-child(1) > div > div > div > a')
			upcoming_match_makeyourstats.click()
			
			driver.switch_to.window(driver.window_handles[1])
			
			dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sidebar-scroll > div > div.pb-1.pt-1.position-sticky.stats-switch > ul > li.nav-item.mx-2.mt-1 > button')))
			
			if dropdown.text == 'Last 5 games':
				dropdown.click()
				all_games = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sidebar-scroll > div > div.pb-1.pt-1.position-sticky.stats-switch > ul > li.nav-item.mx-2.mt-1 > div > a:nth-child(3)')))
				all_games.click()
			else:
				st.write('Nie otwarto wszystkich meczów')
			sleep(1)
			
			try:
				home_all_games = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sidebar-scroll > div > div.pb-1.pt-1.position-sticky.stats-switch > ul > li.nav-item.m-0.mx-1.mt-1 > button')))
				sleep(1)
				home_all_games.click()
			except:
				pass
			
			try:
				away_all_games = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sidebar-scroll > div > div.pb-1.pt-1.position-sticky.stats-switch > ul > li:nth-child(5) > button')))
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
			AWAY_POINT.append(conceded_home_makestats)
			
			try:
				#HOME xG AND xGA
				xg_home_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals (xG)"]/../preceding-sibling::div//span').text 
				xg_home_makestats = float(xg_home_makestats)
				HOME_POINT.append(xg_home_makestats)
				xga_home_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals against (xGA)"]/../preceding-sibling::div//span').text 
				xga_home_makestats = float(xga_home_makestats)
				AWAY_POINT.append(xga_home_makestats)
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
			HOME_POINT.append(conceded_away_makestats)
			
			try:
				#AWAY xG AND xGA
				xg_away_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals (xG)"]/../following-sibling::div//span').text
				xg_away_makestats = float(xg_away_makestats)
				AWAY_POINT.append(xg_away_makestats)	
				xga_away_makestats = driver.find_element(By.XPATH,'//p[normalize-space(text()) = "Expected goals against (xGA)"]/../following-sibling::div//span').text
				xga_away_makestats = float(xga_away_makestats)
				HOME_POINT.append(xga_away_makestats)
			except:
				pass
			
			# try:
			#     st.write(f'Klub: {home_name_makestats}\nStrzelone: {scored_home_makestats}\nStracone: {conceded_home_makestats}\nxG:{xg_home_makestats}\nxGA: {xga_home_makestats}')
			# except:
			#     st.write(f'Klub: {home_name_makestats}\nStrzelone: {scored_home_makestats}\nStracone: {conceded_home_makestats}')
			
			# try:
			#     st.write(f'Klub: {away_name_makestats}\nStrzelone: {scored_away_makestats}\nStracone: {conceded_away_makestats}\nxG:{xg_away_makestats}\nxGA: {xga_away_makestats}')
			# except:
			#     st.write(f'Klub: {away_name_makestats}\nStrzelone: {scored_away_makestats}\nStracone: {conceded_away_makestats}')
			
			
			
			#BESOCCER----------------------------------------------------
			
			r = requests.get(BESOCCER,headers=headers)
			bs = BeautifulSoup(r.content,'lxml')
			url = bs.select('h2.panel-title:-soup-contains("In their next clash")')
			try:
				match_link = bs.find('h2', attrs={"class":"panel-title"}, string="In their next clash").parent.parent.find("a", attrs={"class":"match-link"}).get('href')
			except AttributeError:
				st.error('Wystąpił błąd')
			r = requests.get(f'{match_link}/analysis',headers=headers)
			bs = BeautifulSoup(r.content,'html.parser')
			
			
			#HOME
			home_name_besoccer = bs.select('div.info.match-link > div.team.match-team.left > div.name-box a')[0].text
			xg_home_besoccer = bs.select('div.content-box.t-1 > div.poss-box > div:nth-child(4) > strong')[0].text
			xg_home_besoccer = float(xg_home_besoccer)
			HOME_POINT.append(xg_home_besoccer)
			
			#AWAY
			away_name_besoccer = bs.select('div.info.match-link > div.team.match-team.right > div.name-box a')[0].text
			xg_away_besoccer = bs.select('div.content-box.t-2 > div.poss-box > div:nth-child(4) > strong')[0].text
			xg_away_besoccer = float(xg_away_besoccer)
			AWAY_POINT.append(xg_away_besoccer)
			
			
			#SOCCERRATING-----------------------------------------------------------------------
			driver.get(SOCCERRATING)
			
			
			
			#NAZWA DRUŻYN
			soccerrating_home_name = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[3]/tbody/tr[2]/td/font/table[1]/tbody/tr[1]/td[2]').text
			soccerrating_away_name = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[3]/tbody/tr[2]/td/font/table[1]/tbody/tr[1]/td[3]').text
			
			#KURSY OTWARCIA
			soccerating_open_home_odds = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[3]/tbody/tr[2]/td/font/table[1]/tbody/tr[2]/td[2]').text
			soccerating_open_home_odds = soccerating_open_home_odds.split('(')[1][:-1]
			
			soccerating_open_away_odds = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[3]/tbody/tr[2]/td/font/table[1]/tbody/tr[2]/td[3]').text
			soccerating_open_away_odds = soccerating_open_away_odds.split('(')[1][:-1]
			
			try:
				# OCZEKIWANE SKŁADY CZY WYJŚCIOWE
				status_squad = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[4]/th/font').text
				if status_squad == '▼ Expected Lineup':
					st.markdown('''<div class="alert alert-warning d-flex"> 
		        <i class="bi bi-exclamation-triangle-fill">  
		         Przewidywane składy wyjściowe. Oficjalne składy wkrótce. 
		        </i> 
		    </div> ''', unsafe_allow_html=True)
				else:
					st.markdown('''<div class="alert alert-success d-flex"> 
		        <i class="bi bi-check-circle-fill">  
		         Potwierdzone składy wyjściowe. 
		        </i> 
		    </div> ''', unsafe_allow_html=True)
			
				#STATYSTYKI WYJŚCIOWEGO SKŁADU
				stats_mg = []
				
				home_nazwa = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[5]/td[1]/a[1]').text
				home_stats_mg = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[5]/td[1]').text.split('\n')[1].split(',')[0]
				stats_mg.append(home_stats_mg)
				
				away_nazwa = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[5]/td[2]/a[1]').text
				away_stats_mg = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[5]/td[2]').text.split('\n')[1].split(',')[0]
				stats_mg.append(away_stats_mg)
			
				kontuzje_home = []
				kontuzje_away = []
			
				#KONTUZJE HOME
				flaga = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[1]//tr/td[2]//div[1]/img')
				pilkarz_home = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[1]//tr/td[2]')
				mecze_home = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[1]//tr/td[3]')
				rating_home = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[1]//tr/td[4]')
				flagi_home_kontuzje = []
				for player in range(len(pilkarz_home)):
					src = flaga[player].get_attribute('src')
					flagi_home_kontuzje.append(src)
					info = f'{pilkarz_home[player].text} {mecze_home[player].text}'
					kontuzje_home.append(info)
			
				
			
				sklad_wyjsciowy_home = []
				sklad_rezerwowy_home = []
			
				sklad_wyjsciowy_away = []
				sklad_rezerwowy_away = []
			
				#WYJŚCIOWE SKŁADY HOME
				flaga = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()<12]/td[2]/div[1]/img')
				pilkarz_home_start = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()<12]/td[2]')
				mecze_home_start = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()<12]/td[3]')
				rating_home_start = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()<12]/td[4]')
				flagi_home_start = []
			
				for player in range(len(pilkarz_home_start)):
					src = flaga[player].get_attribute('src')
					flagi_home_start.append(src)
					info = f'{pilkarz_home_start[player].text} {mecze_home_start[player].text}'
					sklad_wyjsciowy_home.append(info)
					
			
				#SKŁADY REZERWOWE HOME
				flaga = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()>12]/td[2]/div[1]/img')
				pilkarz_home_sub = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()>12]/td[2]')
				mecze_home_sub = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()>12]/td[3]')
				rating_home_sub = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[1]//tr[position()>12]/td[4]')
				flagi_home_sub = []
			
				for player in range(len(pilkarz_home_sub)):
					src = flaga[player].get_attribute('src')
					flagi_home_sub.append(src)
					info = f'{pilkarz_home_sub[player].text} {mecze_home_sub[player].text}'
					sklad_rezerwowy_home.append(info)
					
			
				
				#KONTUZJE AWAY
				flaga = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[2]//tr/td[2]//div[1]/img')
				pilkarz_away = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[2]//tr/td[2]')
				mecze_away = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[2]//tr/td[3]')
				rating_away = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]/tbody/tr[3]/td[2]//tr/td[4]')
				flagi_away_kontuzje = []
			
				for player in range(len(pilkarz_away)):
					src = flaga[player].get_attribute('src')
					flagi_away_kontuzje.append(src)
					info = f'{pilkarz_away[player].text} {mecze_away[player].text}'
					kontuzje_away.append(info)
			
				#WYJŚCIOWE SKŁADY AWAY
				flaga = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()<12]/td[2]/div[1]/img')
				pilkarz_away_start = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()<12]/td[2]')
				mecze_away_start = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()<12]/td[3]')
				rating_away_start = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()<12]/td[4]')
				flagi_away_start = []
			
				for player in range(len(pilkarz_home_start)):
					src = flaga[player].get_attribute('src')
					flagi_away_start.append(src)
					info = f'{pilkarz_away_start[player].text} {mecze_away_start[player].text}'
					sklad_wyjsciowy_away.append(info)
			
				#SKŁADY REZERWOWE AWAY
				flaga = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()>12]/td[2]/div[1]/img')
				pilkarz_away_sub = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()>12]/td[2]')
				mecze_away_sub = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()>12]/td[3]')
				rating_away_sub = driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/table[4]//tbody/tr[6]/td[2]//tr[position()>12]/td[4]')
				flagi_away_sub = []
			
				for player in range(len(pilkarz_away_sub)):
					src = flaga[player].get_attribute('src')
					flagi_away_sub.append(src)
					info = f'{pilkarz_away_sub[player].text} {mecze_away_sub[player].text}'
					sklad_rezerwowy_away.append(info)
			
			except:
				st.error('Brak składów')
			
			try:
				html_kontuzje = tabela_kontuzje_rezerwowi(kontuzje_home, kontuzje_away, flagi_home_kontuzje,flagi_away_kontuzje, 'Kontuzje')
				html_wyjsciowy = tabela_kontuzje_rezerwowi(sklad_wyjsciowy_home, sklad_wyjsciowy_away,flagi_home_start,flagi_away_start,"Skład wyjściowy",power=True)
				html_rezerwy =  tabela_kontuzje_rezerwowi(sklad_rezerwowy_home,sklad_rezerwowy_away,flagi_home_sub,flagi_away_sub,"Rezerwowi")
			except:
				st.write(' ')
			
			
			try:
				st.markdown(f'{html_kontuzje + html_wyjsciowy + html_rezerwy  }',unsafe_allow_html=True)
			except:
				pass
			
			tab1, tab2, tab3= st.tabs(["Podobne mecze","Strzelone/Stracone", "Oczekiwane kursy"])
			
			
			
			tabela_home = []
			# MECZE ARCHIWUM + KURSY HOME
			home_ilosc_meczow = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/..')
			home_data = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[2]')
			home_mecz = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[3]')
			home_kurs_home = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[4]')
			home_kurs_draw = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[5]')
			home_kurs_away = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[6]')
			home_rozgrywki = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[8]')
			home_wynik = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text() and not(text()="PSTP") ]/../td[11]')
			
			for i in range(len(home_ilosc_meczow)):
				g = home_data[i].text
				new = f'20{g[-2:]}-{g[3:5]}-{g[:2]}'
				#st.write(f'{new} | {home_mecz[i].text:>48} | {home_kurs_home[i].text} - {home_kurs_draw[i].text} - {home_kurs_away[i].text} | {home_rozgrywki[i].text:>5} | {home_wynik[i].text}')
			
				stats = {
					'Data': new,
					'Mecz': home_mecz[i].text,
					'KursHome': home_kurs_home[i].text,
					'KursDraw': home_kurs_draw[i].text,
					'KursAway': home_kurs_away[i].text,
					'Rozgrywki': home_rozgrywki[i].text,
					'Wynik': home_wynik[i].text,
					'GoleHome': home_wynik[i].text.split(":")[0],
					'GoleAway': home_wynik[i].text.split(":")[1]
				}
				tabela_home.append(stats)
			try:
				df_home = pd.DataFrame(tabela_home)
			except:
				pass
			
			records_home = df_home.to_records(index=False)
			list_of_tuples_home = list(records_home)
			
			#SQLITE DO ARCHIWUM
			conn_match = sqlite3.connect('archive.db')
			cur_match = conn_match.cursor()
			
			#SQL HOME
			try:
				cur_match.execute('DROP TABLE match_home')
			except:
				pass
			
			cur_match.execute(
				'''CREATE TABLE IF NOT EXISTS match_home (
				Id INTEGER PRIMARY KEY AUTOINCREMENT,
				Data TEXT,
				Mecz TEXT,
				KursHome REAL,
				KursDraw REAL,
				KursAway REAL,
				Rozgrywki TEXT,
				Wynik TEXT,
				GoleHome INTEGER,
				GoleAway INTEGER )''')
			
			cur_match.executemany('INSERT INTO match_home (Data, Mecz, KursHome, KursDraw, KursAway, Rozgrywki, Wynik, GoleHome, GoleAway) VALUES (?,?,?,?,?,?,?,?,?)',list_of_tuples_home)
			conn_match.commit()
			
			#PRZEŁĄCZENIE NA DRUZYNE GOŚCI
			try:
				switch_team = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/table[3]/tbody/tr[2]/td/font/table[1]/tbody/tr[1]/td[3]/a')
				switch_team.click()
			except:
				pass
			
			tabela_away = []
			# MECZE ARCHIWUM + KURSY AWAY
			away_ilosc_meczow = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/..')
			away_data = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[2]')
			away_mecz = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[3]')
			away_kurs_home = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[4]')
			away_kurs_draw = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[5]')
			away_kurs_away = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[6]')
			away_rozgrywki = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text()]/../td[8]')
			away_wynik = driver.find_elements(By.XPATH,'/html/body/div[1]/div[4]/table[@class="bigtable"]/tbody/tr/td[last()][text() and not(text()="PSTP")]/../td[11]')
			
			
			for i in range(len(away_ilosc_meczow)):
				g = away_data[i].text
				new = f'20{g[-2:]}-{g[3:5]}-{g[:2]}'
				# st.write(f'{new} | {away_mecz[i].text:>45} | {away_kurs_home[i].text} - {away_kurs_draw[i].text} - {away_kurs_away[i].text} | {away_rozgrywki[i].text:>5} | {away_wynik[i].text}')
			
			
				stats = {
					'Data': new,
					'Mecz': away_mecz[i].text,
					'KursHome': away_kurs_home[i].text,
					'KursDraw': away_kurs_draw[i].text,
					'KursAway': away_kurs_away[i].text,
					'Rozgrywki': away_rozgrywki[i].text,
					'Wynik': away_wynik[i].text,
					'GoleHome': away_wynik[i].text.split(":")[0],
					'GoleAway': away_wynik[i].text.split(":")[1]
				}
				tabela_away.append(stats)
			
			try:
				df_away = pd.DataFrame(tabela_away)
			except:
				pass
			
			records_away = df_away.to_records(index=False)
			list_of_tuples_away = list(records_away)
			
			#SQL AWAY
			try:
				cur_match.execute('DROP TABLE match_away')
			except:
				pass
			
			cur_match.execute(
				'''CREATE TABLE IF NOT EXISTS match_away (
				Id INTEGER PRIMARY KEY AUTOINCREMENT,
				Data TEXT,
				Mecz TEXT,
				KursHome REAL,
				KursDraw REAL,
				KursAway REAL,
				Rozgrywki TEXT,
				Wynik TEXT,
				GoleHome INTEGER,
				GoleAway INTEGER )''')
			
			cur_match.executemany('INSERT INTO match_away (Data, Mecz, KursHome, KursDraw, KursAway, Rozgrywki, Wynik, GoleHome, GoleAway) VALUES (?,?,?,?,?,?,?,?,?)',list_of_tuples_away)
			conn_match.commit()
			st.write('\n')
			
			#AKCEPTOWALNE KURSY
			home_odds = float(soccerating_open_home_odds)
			away_odds = float(soccerating_open_away_odds)
			st.write('\n')
			
			with tab1:
				if home_odds < away_odds:
					min_odds = (home_odds*0.9)-0.1
					min_odds = round(min_odds,2)
					max_odds = (home_odds*1.1)+0.1
					max_odds = round(max_odds,2)
			
					st.markdown(f'''<div class="mx-auto bg-dark text-white text-center">
		   					<p>Faworyt meczu: HOME</p>
							<p>Zakres kursów: {min_odds}-{max_odds}</p>
							</div>''',unsafe_allow_html=True)
			
					#DRUŻYNA GOSPODARZY --------------------------------------------------------------------------------------------------------------------
					
					#TESTOWE
					cur_match.execute(f'''
					SELECT Data, Mecz, KursHome, KursDraw, KursAway, Rozgrywki, Wynik
					FROM match_home
					WHERE Mecz like "{soccerrating_home_name} - %" AND Rozgrywki not like "%CUP%" AND KursHome BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01" ''')
					data = cur_match.fetchall()
					columns = [description[0] for description in cur_match.description]
					html_table = "<table class='table table-responsive table-striped text-center table-dark table-sm'><tr>"
					for column in columns:
						html_table += f"<th>{column}</th>"
					html_table += "</tr>"
					for row in data:
						html_table += "<tr>"
						for value in row:
							html_table += f"<td>{value}</td>"
						html_table += "</tr>"
					html_table += "</table>"
					st.markdown(html_table,unsafe_allow_html=True)
					#KONIEC TESTOWEGO
					
					for row in cur_match.execute(f'''
					SELECT AVG(GoleHome)
					FROM match_home
					WHERE Mecz like "{soccerrating_home_name} - %" AND Rozgrywki not like "%CUP%" AND KursHome BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xG_home = list(row)[0]
							xG_home = round(xG_home,2)
							xG_home = float(xG_home)
							HOME_POINT.append(xG_home)
							st.markdown(f'<div class="p-3 mb-2 bg-success text-white text-center">Strzelone: {xG_home} </div>',unsafe_allow_html=True)
						else:
							continue
			
					for row in cur_match.execute(f'''
					SELECT AVG(GoleAway)
					FROM match_home
					WHERE Mecz like "{soccerrating_home_name} - %" AND Rozgrywki not like "%CUP%" AND KursHome BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xGA_home = list(row)[0]
							xGA_home = round(xGA_home,2)
							xGA_home = float(xGA_home)
							AWAY_POINT.append(xGA_home)
							st.markdown(f'<div class="p-3 mb-2 bg-danger text-white text-center">Stracone: {xGA_home} </div>',unsafe_allow_html=True)
						else:
							continue
			
					
			
					# #DRUŻYNA GOŚCI --------------------------------------------------------------------------------------------------------------------
			
					#TESTOWE
					cur_match.execute(f'''
					SELECT Data, Mecz, KursHome, KursDraw, KursAway, Rozgrywki, Wynik
					FROM match_away
					WHERE Mecz like "% - {soccerrating_away_name}" AND Rozgrywki not like "%CUP%" AND KursHome BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												''')
					data = cur_match.fetchall()
					columns = [description[0] for description in cur_match.description]
					html_table = "<table class='table table-responsive table-striped text-center table-dark table-sm'><tr>"
					for column in columns:
						html_table += f"<th>{column}</th>"
					html_table += "</tr>"
					for row in data:
						html_table += "<tr>"
						for value in row:
							html_table += f"<td>{value}</td>"
						html_table += "</tr>"
					html_table += "</table>"
					st.markdown(html_table,unsafe_allow_html=True)
					#KONIEC TESTOWEGO
					
					for row in cur_match.execute(f'''
					SELECT AVG(GoleAway)
					FROM match_away
					WHERE Mecz like "% - {soccerrating_away_name}" AND Rozgrywki not like "%CUP%" AND KursHome BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xG_away = list(row)[0]
							xG_away = round(xG_away,2)
							xG_away = float(xG_away)
							AWAY_POINT.append(xG_away)
							st.markdown(f'<div class="p-3 mb-2 bg-success text-white text-center">Strzelone: {xG_away} </div>',unsafe_allow_html=True)
						else:
							continue
			
					for row in cur_match.execute(f'''
					SELECT AVG(GoleHome)
					FROM match_away
					WHERE Mecz like "% - {soccerrating_away_name}" AND Rozgrywki not like "%CUP%" AND KursHome BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xGA_away= list(row)[0]
							xGA_away = round(xGA_away,2)
							xGA_away = float(xGA_away)
							HOME_POINT.append(xGA_away)
							st.markdown(f'<div class="p-3 mb-2 bg-danger text-white text-center">Stracone: {xGA_away} </div>',unsafe_allow_html=True)
						else:
							continue
			
			
				# GDY FAWORYT GOŚCIE --------------------------------------------------------------------------------------------------------------------
				else:
					min_odds = (away_odds*0.9)-0.1
					min_odds = round(min_odds,2)
					max_odds = (away_odds*1.1)+0.1
					max_odds = round(max_odds,2)
			
					st.markdown(f'''<div class="mx-auto bg-dark text-white text-center">
		   					<p>Faworyt meczu: AWAY</p>
							<p>Zakres kursów: {min_odds}-{max_odds}</p>
							</div>''',unsafe_allow_html=True)
					
					#DRUŻYNA GOSPODARZY --------------------------------------------------------------------------------------------------------------------
					
			
					#TESTOWE
					cur_match.execute(f'''
					SELECT Data, Mecz, KursHome, KursDraw, KursAway, Rozgrywki, Wynik
					FROM match_away
					WHERE Mecz like "% - {soccerrating_away_name}" AND Rozgrywki not like "%CUP%" AND KursAway BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												''')
					data = cur_match.fetchall()
					columns = [description[0] for description in cur_match.description]
					html_table = "<table class='table table-responsive table-striped text-center table-dark table-sm'><tr>"
					for column in columns:
						html_table += f"<th>{column}</th>"
					html_table += "</tr>"
					for row in data:
						html_table += "<tr>"
						for value in row:
							html_table += f"<td>{value}</td>"
						html_table += "</tr>"
					html_table += "</table>"
					st.markdown(html_table,unsafe_allow_html=True)
					#KONIEC TESTOWEGO
					for row in cur_match.execute(f'''
					SELECT AVG(GoleAway)
					FROM match_away
					WHERE Mecz like "% - {soccerrating_away_name}" AND Rozgrywki not like "%CUP%" AND KursAway BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xG_away = list(row)[0]
							xG_away = round(xG_away,2)
							xG_away = float(xG_away)
							st.markdown(f'<div class="p-3 mb-2 bg-success text-white text-center">Strzelone: {xG_away} </div>',unsafe_allow_html=True)
			
					
					
					for row in cur_match.execute(f'''
					SELECT AVG(GoleHome)
					FROM match_away
					WHERE Mecz like "% - {soccerrating_away_name}" AND Rozgrywki not like "%CUP%" AND KursAway BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xGA_away = list(row)[0]
							xGA_away = round(xGA_away,2)
							xGA_away = float(xGA_away)
							st.markdown(f'<div class="p-3 mb-2 bg-danger text-white text-center">Stracone: {xGA_away} </div>',unsafe_allow_html=True)
						else:
							continue
			
					
					st.write('-'*40)
			
					# #DRUŻYNA GOŚCI --------------------------------------------------------------------------------------------------------------------
					
					#TESTOWE
					cur_match.execute(f'''
					SELECT Data, Mecz, KursHome, KursDraw, KursAway, Rozgrywki, Wynik
					FROM match_home
					WHERE Mecz like "{soccerrating_home_name} - %" AND Rozgrywki not like "%CUP%" AND KursAway BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												''')
					data = cur_match.fetchall()
					columns = [description[0] for description in cur_match.description]
					html_table = "<table class='table table-responsive table-striped text-center table-dark table-sm'><tr>"
					for column in columns:
						html_table += f"<th>{column}</th>"
					html_table += "</tr>"
					for row in data:
						html_table += "<tr>"
						for value in row:
							html_table += f"<td>{value}</td>"
						html_table += "</tr>"
					html_table += "</table>"
					st.markdown(html_table,unsafe_allow_html=True)
					#KONIEC TESTOWEGO
					for row in cur_match.execute(f'''
					SELECT AVG(GoleHome)
					FROM match_home
					WHERE Mecz like "{soccerrating_home_name} - %" AND Rozgrywki not like "%CUP%" AND KursAway BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xG_home = list(row)[0]
							xG_home = round(xG_home,2)
							xG_home = float(xG_home)
							st.markdown(f'<div class="p-3 mb-2 bg-success text-white text-center">Strzelone: {xG_home} </div>',unsafe_allow_html=True)
			
			
					for row in cur_match.execute(f'''
					SELECT AVG(GoleAway)
					FROM match_home
					WHERE Mecz like "{soccerrating_home_name} - %" AND Rozgrywki not like "%CUP%" AND KursAway BETWEEN {min_odds} AND {max_odds} AND Data >= "2022-07-01"
												'''):
						if row[0] is not None:							
							xGA_home= list(row)[0]
							xGA_home = round(xGA_home,2)
							xGA_home = float(xGA_home)
							st.markdown(f'<div class="p-3 mb-2 bg-danger text-white text-center">Stracone: {xGA_home} </div>',unsafe_allow_html=True)
			
			with tab2:
				# DRUŻYNA GOSPODARZY
				strzelone_home.append(xg_home_apwin)
				strzelone_home.append(scored_home_makestats)
				try:
					strzelone_home.append(xg_home_makestats)
				except:
					pass
				strzelone_home.append(xg_home_besoccer)
				try:
					strzelone_home.append(xG_home)
				except:
					strzelone_home.append(1)
					
				
				
				stracone_home.append(xga_home_apwin)
				stracone_home.append(conceded_home_makestats)
				try:
					stracone_home.append(xga_home_makestats)
				except:
					pass
		
				try:
					stracone_home.append(xGA_home)
				except:
					stracone_home.append(1)
			
				# DRUŻYNA GOŚCI
				strzelone_away.append(xg_away_apwin)
				strzelone_away.append(scored_away_makestats)
				try:
					strzelone_away.append(xg_away_makestats)
				except:
					pass
				strzelone_away.append(xg_away_besoccer)
				try:
					strzelone_away.append(xG_away)
				except:
					strzelone_away.append(1)
				
				
				stracone_away.append(xga_away_apwin)
				stracone_away.append(conceded_away_makestats)
				try:
					stracone_away.append(xga_away_makestats)
				except:
					pass
		
				try:
					stracone_away.append(xGA_away)
				except:
					stracone_away.append(1)
				
				styl_wyswietl = '''<style>table#wyswietl,th,td {
			 font-size: 12px;
			 /*width: 100%;*/
			 font-family: Poppins;
			 border-collapse: collapse;
			 text-align:center;
			 border-bottom: 2px solid black;
			 padding: 3px;
			 }
			 
			 /*table#wyswietl {
			 margin: 0px auto;
			 align-items: center;
			 justify-content: center;
			 
			 }*/
			 
			 th {
			 background-color: #7A7978;
			 font-weight: 500;
			 }
			 
			 td.stracone {
			 background-color: #CC8989;
			 }
			 td.scored {
			 background-color: #87CBAC;
			 } </style>'''
				tab_wyswietl = tabela_wyswietl()
				st.markdown(styl_wyswietl + tab_wyswietl,unsafe_allow_html=True)
				
							
							
			  
				# st.markdown(f'''{"Strzelone":>40} {"Stracone":>50}
				# {home_name_apwin:<20} {xg_home_apwin,scored_home_makestats,xg_home_makestats,xg_home_besoccer,xG_home} {"":>19} {xga_home_apwin,conceded_home_makestats,xga_home_makestats,xGA_home}
				# {away_name_apwin:<20} {xg_away_apwin,scored_away_makestats,xg_away_makestats,xg_away_besoccer,xG_away} {"":>20} {xga_away_apwin,conceded_away_makestats,xga_away_makestats,xGA_away} ''')
		
			from statistics import mean
			
			xg_gospodarze = mean(HOME_POINT)
			xg_gospodarze = round(xg_gospodarze,2)
			
			xg_goscie = mean(AWAY_POINT)
			xg_goscie = round(xg_goscie,2)
			
			
			#------------------------ TABELA NA KURSY
			
			win = []
			dc = []
			gole0 = ['0.5']
			gole1 = ['1.5']
			gole2 = ['2.5']
			gole3 = ['3.5']
			gole4 = ['4.5']
			dnb = ['AH0']
			bts = ['']
			home0 = ['0.5']
			home1 = ['1.5']
			away0 = ['0.5']
			away1 = ['1.5']
			
			#----------—-------------
			
			driver.get('https://xgscore.io/apps/odds-calculator')
			
			home = driver.find_element(By.XPATH,'//input[@id="home-team"]')
			home.clear()
			home.send_keys(xg_gospodarze)
			
			away = driver.find_element(By.XPATH,'//input[@id="away-team"]')
			away.clear()
			away.send_keys(xg_goscie)
			sleep(1)
			odds = driver.find_element(By.XPATH,'//*[@id="mat-button-toggle-2-button"]/span')
			odds.click()
			
			#-------------------- 1x2
			kurs_home = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[1]/div[2]/div[1]/div[2]').text
			kurs_draw = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[1]/div[2]/div[2]/div[2]').text
			kurs_away = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[1]/div[2]/div[3]/div[2]').text
			
			win.append(kurs_home)
			win.append(kurs_draw)
			win.append(kurs_away)
			
			# #-------------------- PODWÓJNA SZANSA
			kurs_dc_1x = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[2]/div[2]/div[1]/div[2]').text
			kurs_dc_12 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[2]/div[2]/div[2]/div[2]').text
			kurs_dc_x2 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[2]/div[2]/div[3]/div[2]').text
			
			dc.append(kurs_dc_1x)
			dc.append(kurs_dc_12)
			dc.append(kurs_dc_x2)
			
			# #-------------------- GOLE
			kurs_O05 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[2]/div[1]/div[2]').text
			kurs_U05 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[2]/div[2]/div[2]').text
			
			gole0.insert(0,kurs_O05)
			gole0.insert(2,kurs_U05)
			
			
			kurs_O1 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[3]/div[1]/div[2]').text
			kurs_U1 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[3]/div[2]/div[2]').text
			
			
			
			kurs_O15 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[4]/div[1]/div[2]').text
			kurs_U15 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[4]/div[2]/div[2]').text
			
			gole1.insert(0,kurs_O15)
			gole1.insert(2,kurs_U15)
			
			kurs_O2 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[5]/div[1]/div[2]').text
			kurs_U2 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[5]/div[2]/div[2]').text
			
			kurs_O25 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[6]/div[1]/div[2]').text
			kurs_U25 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[6]/div[2]/div[2]').text
			
			gole2.insert(0,kurs_O25)
			gole2.insert(2,kurs_U25)
			
			kurs_O3 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[7]/div[1]/div[2]').text
			kurs_U3 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[7]/div[2]/div[2]').text
			
			kurs_O35 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[8]/div[1]/div[2]').text
			kurs_U35 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[8]/div[2]/div[2]').text
			
			gole3.insert(0,kurs_O35)
			gole3.insert(2,kurs_U35)
			
			kurs_O4 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[9]/div[1]/div[2]').text
			kurs_U4 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[9]/div[2]/div[2]').text
			
			kurs_O45 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[10]/div[1]/div[2]').text
			kurs_U45 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[3]/div[1]/div/div[10]/div[2]/div[2]').text
			
			gole4.insert(0,kurs_O45)
			gole4.insert(2,kurs_U45)
			
			# #-------------------- Handicap DNB
			kurs_dnb_home = driver.find_element(By.XPATH, '//span[text()=" Home (0) "]/../../div[2]').text
			kurs_dnb_away = driver.find_element(By.XPATH, '//span[text()=" Away (0) "]/../../div[2]').text
			
			dnb.insert(0,kurs_dnb_home)
			dnb.insert(2,kurs_dnb_away)
			
			
			
			# #-------------------- BTS
			
			kurs_bts_yes = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[4]/div[2]/div[1]/div[2]').text
			kurs_bts_no = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[4]/div[2]/div[2]/div[2]').text
			
			bts.insert(0,kurs_bts_yes)
			bts.insert(2,kurs_bts_no)
			
			# #-------------------- GOLE INDYWIDUALNE
			kurs_home_over_05 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[1]/div/div[2]/div[1]/div[2]').text
			kurs_home_under_05 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[1]/div/div[2]/div[2]/div[2]').text
			kurs_home_over_15 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[1]/div/div[4]/div[1]/div[2]').text
			kurs_home_under_15 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[1]/div/div[4]/div[2]/div[2]').text
			
			home0.insert(0,kurs_home_over_05)
			home0.insert(2,kurs_home_under_05)
			
			home1.insert(0,kurs_home_over_15)
			home1.insert(2,kurs_home_under_15)
			
			
			
			
			
			kurs_away_over_05 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[2]/div/div[2]/div[1]/div[2]').text
			kurs_away_under_05 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[2]/div/div[2]/div[2]/div[2]').text
			kurs_away_over_15 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[2]/div/div[4]/div[1]/div[2]').text
			kurs_away_under_15 = driver.find_element(By.XPATH, '/html/body/xgs-root/div/div/div/xgs-apps/xgs-page-wrapper/main/xgs-odds-calculator/xgs-old-odds/div/div[5]/div[2]/div/div[4]/div[2]/div[2]').text
			
			away0.insert(0,kurs_away_over_05)
			away0.insert(2,kurs_away_under_05)
			
			away1.insert(0,kurs_away_over_15)
			away1.insert(2,kurs_away_under_15)
			
			with tab3:
				st.markdown(f'<h4 class="text-center text-white">{xg_gospodarze} - {xg_goscie}</h4>',unsafe_allow_html=True)
				tab = tabela_kursy() 
				st.markdown(f'{tab}', unsafe_allow_html=True) 
			
			
			st.markdown('''<div class="alert alert-success text-center" role="alert">Analiza zakończona!</div>''', unsafe_allow_html=True)
			KONIEC = datetime.now() + timedelta(hours=1)
			
			t = KONIEC - START
			t = str(t)
			ti = t.split('.')
		
			st.markdown(f'<p class="h6 text-center text-white">Czas analizy {ti[0]}</p>',unsafe_allow_html=True)
		#conn.close()
	
	with menu1:
		st.markdown(f'''<div class="container-fluid p-5 bg-primary text-white text-center">
	 					<h2>Obsługiwane ligi</h2>
		  				<p class="pt-1">Lista aktualnie obsługiwanych lig.</p>
		   				</div> 
				<div class="container-fluid text-center text-white">
	   			<h4 class="text-center text-white">Propozycja ligi</h4></div>''',unsafe_allow_html=True)
		st.text_input('Wpisz ligę')
		#DZIALAJACE POBIERANIE KRAJOW I LIG JAKIE OBSLUGUJE PROGRAM
		# Utworzenie połączenia z bazą danych
		
		
		# Pobranie danych z bazy
		c.execute("SELECT DISTINCT KRAJ FROM list_teams ORDER BY KRAJ")
		kraje = c.fetchall()
		
		# Generowanie listy HTML
		html = "<ul>"
		for kraj in kraje:
		    html += f"<li class='h2 fw-bold'>{kraj[0]}"
		    
		    c.execute("SELECT DISTINCT LIGA FROM list_teams WHERE kraj = ?", (kraj[0],))
		    miasta = c.fetchall()
		    
		    html += "<ul>"
		    for miasto in miasta:
		        html += f"<li>{miasto[0]}</li>"
		    html += "</ul>"
		    
		    html += "</li>"
		html += "</ul>"
		
		st.markdown(html,unsafe_allow_html=True)
		
	
	with menu2:
		st.markdown(''' ''',unsafe_allow_html=True)
		
		c.execute('''CREATE TABLE IF NOT EXISTS errors 
	             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
	              error_text TEXT, 
	              error_date TEXT)''')
		# Formularz zgłaszania błędów
		st.write("# Formularz zgłaszania błędów")
		error_text = st.text_area("Opisz znaleziony błąd:")
		if st.button("Zgłoś"):
			error_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			c.execute("INSERT INTO errors (error_text, error_date) VALUES (?, ?)", (error_text, error_date))
			conn.commit()
			st.markdown('''<div class="alert alert-success text-center" role="alert">Błąd został zgłoszony pomyślnie!</div>''', unsafe_allow_html=True) 
	
		# Wyświetlanie błędów z bazy danych
		st.write("# Lista zgłoszonych błędów")
		if st.button("Pokaż błędy"):
			errors = c.execute("SELECT * FROM errors").fetchall()
			for error in errors:
				st.write(f"ID: {error[0]}, Opis błędu: {error[1]}, Data zgłoszenia: {error[2]}")
		
