import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Ustawiamy opcje dla przeglądarki, aby uruchamiała się w trybie bezgłowym
chrome_options = Options()
chrome_options.add_argument("--headless")

# Uruchamiamy przeglądarkę w trybie bezgłowym
driver = webdriver.Chrome(options=chrome_options)

# Funkcja do pobierania tytułu strony
def get_page_title(url):
    driver.get(url)
    return driver.title

# Wyświetlamy interfejs użytkownika
st.title("Pobieranie tytułu strony za pomocą Selenium i Streamlit")
url = st.text_input("Wprowadź adres URL strony")

if st.button("Pobierz tytuł strony"):
    if url:
        page_title = get_page_title(url)
        st.write(f"Tytuł strony to: {page_title}")
    else:
        st.write("Wprowadź adres URL strony")
