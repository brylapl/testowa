from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from flask import Flask, render_template
import streamlit.components.v1 as components
import sqlite3
    

st.title("Test")
# Tekst do wyświetlenia
text = "To jest wyśrodkowany tekst na stronie!"

# Użycie HTML do wyśrodkowania tekstu
st.markdown(
    f"<h1 style='text-align: center;'>{text}</h1>",
    unsafe_allow_html=True
)



# Połączenie z bazą danych
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Zapytanie o unikalne kraje
cursor.execute("SELECT DISTINCT kraj FROM geo")
countries = [row[0] for row in cursor.fetchall()]

# Tytuł aplikacji
st.title("Wybór kraju i miasta")

# Lista rozwijana z krajami
country = st.selectbox("Wybierz kraj:", countries)

# Lista rozwijana z miastami, uzależniona od wyboru kraju
if country:
    cursor.execute("SELECT miasto FROM geo WHERE kraj = ?", (country,))
    cities = [row[0] for row in cursor.fetchall()]
    city = st.selectbox("Wybierz miasto:", cities)

# Pokazanie wybranego kraju i miasta
if 'city' in locals():  # Sprawdź, czy zmienna city została zdefiniowana
    st.write(f"You selected: **{country}** and **{city}**")

# Zamknij połączenie z bazą danych
conn.close()


#-----------------------------------------------------------------------------------------------------------  DZIAŁAJĄCY PODWÓJNY FILTR ZE SŁOWNIKA
# tekst = st.text_input("Wpisz tekst")
# if tekst:
#     new_txt = tekst.split(" ")
#     for i in new_txt:
#         st.write(f"Wybrano {i}")
# else:
#     st.error("Wpisz coś")

# # Przykładowy HTML
# dzis = st.date_input("Wybierz date")
# # Słownik z krajami i miastami
# data = {
#     "Polska": ["Warszawa", "Kraków", "Wrocław", "Poznań"],
#     "Niemcy": ["Berlin", "Monachium", "Hamburg", "Frankfurt"],
#     "Francja": ["Paryż", "Lyon", "Marsylia", "Tuluza"],
#     "Hiszpania": ["Madryt", "Barcelona", "Walencja", "Malaga"],
#     "Włochy": ["Rzym", "Mediolan", "Neapol", "Turyn"]
# }

# # Tytuł aplikacji
# st.title("Wybór kraju i miasta")

# # Lista rozwijana z krajami
# country = st.selectbox("Wybierz kraj:", list(data.keys()))

# # Lista rozwijana z miastami, uzależniona od wyboru kraju
# if country:
#     city = st.selectbox("Wybierz miasto:", data[country])

# # Pokazanie wybranego kraju i miasta
# st.write(f"You selected: **{country}** and **{city}**")

# if city:
#     st.title(city)

# html_code = f"""
# <p> Dziś mamy {dzis}.
# """

# components.html(html_code)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# options = Options()
# options.add_argument("--headless=new")
# options.add_argument('--verbose')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument("--window-size=1920x1080")
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
# driver = webdriver.Chrome(options=options)

# url = st.text_input("podaj adres strony")
# start = st.button('START')
# if start:
#     driver.get(url)
#     driver.quit()


