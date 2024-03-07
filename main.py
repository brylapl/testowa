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
    st.write("TREŚĆ WIDOCZNA TYLKO DLA MNIE")
    
    def create_table():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
        conn.commit()
        conn.close()
    
    def add_user(name, email):
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', (name, email))
        conn.commit()
        conn.close()
    
    def read_users():
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users''')
        users = c.fetchall()
        conn.close()
        return users
    
    def update_user(id, name, email):
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute('''UPDATE users SET name=?, email=? WHERE id=?''', (name, email, id))
        conn.commit()
        conn.close()
    
    def delete_user(id):
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute('''DELETE FROM users WHERE id=?''', (id,))
        conn.commit()
        conn.close()
    # Create table if it doesn't exist
    create_table()

    st.title('CRUD Database Management')
    # Add user form
    st.subheader('Add User')
    name = st.text_input('Name')
    email = st.text_input('Email')
    if st.button('Add User'):
        add_user(name, email)\
        st.success('User added successfully!')
    
    st.subheader('All Users')
    users = read_users()
    for user in users:
        st.write(f'ID: {user[0]}, Name: {user[1]}, Email: {user[2]}')

# # Update user form
# st.subheader('Update User')
# update_id = st.number_input('ID to Update')
# new_name = st.text_input('New Name')
# new_email = st.text_input('New Email')
# if st.button('Update User'):
#     update_user(update_id, new_name, new_email)
#     st.success('User updated successfully!')

# # Delete user form
# st.subheader('Delete User')
# delete_id = st.number_input('ID to Delete')
# if st.button('Delete User'):
#     delete_user(delete_id)
#     st.success('User deleted successfully!')
    
    # Tutaj umieść kod panelu administracyjnego
    if st.button("Logout"):
        st.success("Zostałeś wylogowany!")
        return False

# Strona startowa
def strona_startowa():
    st.title("STRONA GŁÓWNA")
    st.write("TREŚĆ WIDOCZNA DLA WSZYSTKICH.")

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
