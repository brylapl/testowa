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
#-------------------------------------------------------------------------------------------
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
st.header('baza danych')

import streamlit as st

# Panel logowania dla administratora
def panel_logowania():
    st.sidebar.header("Panel logowania")
    
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        if username == "admin" and password == "admin123":
            st.sidebar.success("Zalogowano pomyślnie!")
            return True
        else:
            st.sidebar.error("Błąd logowania. Spróbuj ponownie.")
            return False

# Panel administracyjny
def panel_administracyjny():
    st.title("Panel administracyjny")
    st.write("Witaj Administratorze!")
    # Tutaj umieść kod panelu administracyjnego

# Strona startowa
def strona_startowa():
    st.title("Witaj na stronie startowej")
    st.write("Cześć, tutaj możesz zobaczyć przykładową stronę startową.")

# Main
def main():
    if panel_logowania():
        panel_administracyjny()
    else:
        strona_startowa()

if __name__ == "__main__":
    main()




# # Panel logowania dla administratora
# def panel_logowania():
#     st.sidebar.header("Panel logowania")
    
#     username = st.sidebar.text_input("Username")
#     password = st.sidebar.text_input("Password", type="password")
    
#     if st.sidebar.button("Login"):
#         if username == "admin" and password == "admin123":
#             st.sidebar.success("Zalogowano pomyślnie!")
#             return True
#         else:
#             st.sidebar.error("Błąd logowania. Spróbuj ponownie.")
#             return False


# # Panel administracyjny
# def panel_administracyjny():
#     st.title("Panel administracyjny")
#     # Tutaj umieść kod panelu administracyjnego
#     if st.button("Logout"):
#         st.success("Zostałeś wylogowany!")
#         return False

# # Strona startowa
# def strona_startowa():
#     st.title("STRONA STARTOWA")
#     st.write("ZAWARTOŚĆ WIDOCZNA DLA WSZYTSTKICH")

# # Main
# def main():
#     if panel_logowania():
#         strona_startowa()
#         if panel_administracyjny():
#             strona_startowa()
#     else:
#         strona_startowa()

# if __name__ == "__main__":
#     main() 





# ----------------------------------------------------------------------------------------------
# # Panel logowania dla administratora
# def panel_logowania():
#     st.sidebar.header("Panel logowania")
    
#     username = st.sidebar.text_input("Username")
#     password = st.sidebar.text_input("Password", type="password")
    
#     if st.sidebar.button("Login"):
#         if username == "admin" and password == "admin123":
#             st.sidebar.success("Zalogowano pomyślnie!")
#             return True
#         else:
#             st.sidebar.error("Błąd logowania. Spróbuj ponownie.")
#             return False

# # Panel administracyjny
# def panel_administracyjny():
#     st.title("Panel administracyjny")
#     st.write("Witaj Administratorze!")
#     # Tutaj umieść kod panelu administracyjnego

# # Strona startowa
# def strona_startowa():
#     st.title("Witaj na stronie startowej")
#     st.write("Cześć, tutaj możesz zobaczyć przykładową stronę startową.")

# # Main
# def main():
#     if panel_logowania():
#         panel_administracyjny()
#     else:
#         strona_startowa()

# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------------------------------------





































# # definiowanie danych logowania
# login_credentials = {
#     "admin": "admin123",
#     "user": "user123"
# }

# # funkcja do sprawdzania danych logowania
# def authenticate(username, password):
#     if username in login_credentials and login_credentials[username] == password:
#         return True
#     else:
#         return False

# # wyświetlanie panelu logowania
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# if st.button("Login"):
#     if authenticate(username, password):
#         st.success("Logged in successfully!")
#         st.session_state.logged_in = True
#     else:
#         st.error("Niepoprawny login lub hasło. Spróbuj ponownie.")

# # przekierowanie do panelu administracji po zalogowaniu
# if "logged_in" in st.session_state:
#     if st.session_state.logged_in:
#         st.write("Tutaj jest panel administracyjny")
