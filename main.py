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
import mysql.connector
from contact import contact
#-------------------------------------------------------------------------------------------
from streamlit_option_menu import option_menu
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="centered", initial_sidebar_state="collapsed", menu_items=None)
#------------------------------------------------------------------------------------------------
#STYLE CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------

# # 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
    
# selected5 = option_menu(None, ["Home", "Calculator", "Contact", 'About'],
#                         icons=['bi-house-door-fill', 'bi-file-bar-graph-fill', "bi-envelope-at-fill", 'bi-info-square-fill'],
#                         on_change=on_change, key='menu_5', orientation="horizontal")

# if selected5 == "Home":
#     st.write("You selected the Home page")    
# elif selected5 == "Upload":
#     st.write("You selected the Upload page")
# elif selected5 == "Contact":
#     with open("contact.html", "r") as file:
#         con = file.read()
#         st.markdown(con, unsafe_allow_html=True)
#     contact()
# elif selected5 == "About":
#     with open("about.html", "r") as file:
#         about_content = file.read()
#         st.markdown(about_content, unsafe_allow_html=True)

def btn():
    btn = st.button('Uruchom')

st.markdown("""<style>
.section-border {
border-bottom: 1px solid rgba(153, 153, 153, 0.2);
}

.section {
position: relative;
}

*, *::before, *::after {
box-sizing: border-box;
}

div {
display: block;
}

.content-wrap {
padding: 100px 0;
}

@media (min-width: 992px)
.container {
max-width: 960px;
}

.container {
width: 100%;
padding-right: 15px;
padding-left: 15px;
margin-right: auto;
margin-left: auto;
}

.align-items-center {
-ms-flex-align: center !important;
align-items: center !important;
}

.row {
display: -ms-flexbox;
display: flex;
-ms-flex-wrap: wrap;
flex-wrap: wrap;
margin-right: -15px;
margin-left: -15px;
}

@media (min-width: 992px)
.col-lg-6 {
-ms-flex: 0 0 50%;
flex: 0 0 50%;
max-width: 50%;
}

.mb-3, .my-3 {
margin-bottom: 1rem !important;
}

.img-fluid {
max-width: 100%;
height: auto;
}

@media (min-width: 992px)
.col-lg-6 {
-ms-flex: 0 0 50%;
flex: 0 0 50%;
max-width: 50%;
}

.supheading {
font-size: 18px;
letter-spacing: 1px;
margin-bottom: 10px;
color: #999999;
}

p {
margin: 0 0 20px 0;
color: #999999;
}

.section-heading, .rs-feature-box-1 .title {
font-size: 60px;
line-height: 1.2em;
margin-bottom: 20px;
margin-top: 0;
padding-bottom: 5px;
position: relative;
color: #222;
font-weight: 400;
}

p {
display: block;
margin-block-start: 1em;
margin-block-end: 1em;
margin-inline-start: 0px;
margin-inline-end: 0px;
}

.spacer-10 {
height: 10px;
}

ul.bull {
margin: 0 0 20px;
list-style: none;
padding: 0;
color: #999999;
}

ul.bull li {
position: relative;
padding: 0 0 0 26px;
margin: 0 0 14px;
}
</style>""",unsafe_allow_html=True)

st.markdown('''
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Strona główna</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

</head>
<body>
<div class="section section-border">
<div class="content-wrap">
<div class="container">

<div class="row align-items-center">	

<div class="col-sm-12 col-md-12 col-lg-6">

<img src="https://html.rometheme.pro/knox/01/images/app-img-1.png" alt="" class="img-fluid mb-3">

</div>					

<div class="col-sm-12 col-md-12 col-lg-6">
<p class="supheading text-cente">No Coding Required</p>
<h2 class="section-heading">
    Develop with KNOX HTML Template
</h2>

<p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium dolore mque laudantium, totam rem aperiam, eaque ipsa quae ab illo invent.</p>
<div class="spacer-10"></div>
<ul class="bull">
    <li>Offer a broad range of cost-effective industrial solutions</li>
    <li>Maintain a robust inventory of parts and products</li>
    <li>Remain responsive to our customers’ needs</li>
</ul>
<div class="spacer-10"></div>
<a href="#" class="btn btn-primary">View Works</a>

</div>									

</div>

</div>
</div>
</div>

</body>
</html>

''', unsafe_allow_html=True)
btn()
