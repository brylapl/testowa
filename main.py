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

st.set_page_config(page_title='Testowe', page_icon=":soccer:", layout="wide", initial_sidebar_state="collapsed", menu_items=None)
#------------------------------------------------------------------------------------------------
#STYLE CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#HTML
#with open("html/index.html", "r") as file:
#index = file.read()
#st.markdown(index, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#CONTACT
#with open("html/contacts.html", "r") as file:
#contacts = file.read()
#st.markdown(contacts, unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------
#contact()
#------------------------------------------------------------------------------------------------
st.markdown("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mobile App Screen</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<style> 
.menu { 
display: flex; 
justify-content: center; 
list-style: none; 
padding: 0; } 
.menu li { 
margin: 0 10px; 
} 
.content { 
padding: 20px; 
} 
@media only screen and (min-width: 768px) { 
.navbar { 
background-color: #007bff; 
color: white; 
padding: 10px 0;
justify-content: space-evenly;
} 
.nav-link { 
color: white !important; 
padding: 0 10px !important; 
} 
} 
@media only screen and (max-width: 767px) { 
.navbar { 
position: fixed; 
bottom: 0; 
width: 100%; 
background-color: #007bff; 
color: white; 
display: flex; 
justify-content: space-evenly; 
padding: 10px 0; 
} 
.nav-link { 
color: white !important; 
padding: 0 10px !important; 
} 
} 
</style>

<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">

<body>
<div class="container-fluid">
<nav class="navbar">

<button class="btn nav-link" onclick="showScreen('screen1')">Home <i class="bi bi-house-door"></i></button>
<button class="btn nav-link" onclick="showScreen('screen2')">Tables <i class="bi bi-table"></i></button>
<button class="btn nav-link" onclick="showScreen('screen3')">Contact <i class="bi bi-telephone"></i></button>
</nav>
</div>
<div class="container">
<div class="content" id="screen1">


<div class="container-fluid px-4 py-5 my-5 text-center">
<div class="lc-block d-block mx-auto mb-4">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" width="5em" height="5em" lc-helper="svg-icon" fill="currentColor">
<path d="M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm121.8 169.9l-40.7 191.8c-3 13.6-11.1 16.9-22.4 10.5l-62-45.7-29.9 28.8c-3.3 3.3-6.1 6.1-12.5 6.1l4.4-63.1 114.9-103.8c5-4.4-1.1-6.9-7.7-2.5l-142 89.4-61.2-19.1c-13.3-4.2-13.6-13.3 2.8-19.7l239.1-92.2c11.1-4 20.8 2.7 17.2 19.5z"></path>
</svg>
</div>
<div class="lc-block">
<div editable="rich">

<h2 class="display-5 fw-bold">The quick brown fox jumps over the lazy dog</h2>

</div>
</div>
<div class="lc-block col-lg-6 mx-auto mb-4">
<div editable="rich">

<p class="lead ">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>

</div>
</div>

<div class="lc-block d-grid gap-2 d-sm-flex justify-content-sm-center"> <a class="btn btn-primary btn-lg px-4 gap-3" href="tables.html" role="button">Click me, I'm a button</a>
<a class="btn btn-outline-secondary btn-lg px-4" href="#" role="button">Click me, I'm a button</a>
</div>
</div>

</div>
<div class="content" id="screen2" style="display: none;">

<div class="container">
<div class="row mb-4 align-items-center">
<div class="col-lg-6 mb-4 mb-lg-0">
<div class="lc-block text-center">
<img class="img-fluid " src="https://cdn.livecanvas.com/media/svg/isometric/app_development_SVG.svg" width="400" height="400" loading="lazy">
</div><!-- /lc-block -->
</div><!-- /col -->
<div class="col-lg-6 p-lg-6">
<div class="lc-block mb-5">
<div editable="rich">

<h2 class="display-6 fw-bold">Boost your Creativity</h2>

<p class="lead"><br>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a lacus est. Etiam diam metus.</p>
</div>
</div><!-- /lc-block -->
<!-- /lc-block -->
<div class="lc-block">
<div class="d-inline-flex">
<div>
<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="text-primary" viewBox="0 0 16 16" lc-helper="svg-icon">
<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"></path>
</svg>
</div>

<div class="ms-3 align-self-center" editable="rich">
<p>Lorem ipsum dolor sit amet</p>
</div>
</div>
</div>
<div class="lc-block">
<div class="d-inline-flex">
<div>
<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="text-primary" viewBox="0 0 16 16" lc-helper="svg-icon">
<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"></path>
</svg>
</div>

<div class="ms-3 align-self-center" editable="rich">
<p>Consectetur adipiscing elit.</p>
</div>
</div>
</div>
<div class="lc-block">
<div class="d-inline-flex">
<div>
<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="text-primary" viewBox="0 0 16 16" lc-helper="svg-icon">
<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"></path>
</svg>
</div>

<div class="ms-3 align-self-center" editable="rich">
<p>Aenean vel nisi in ipsum congue</p>
</div>
</div>
</div><!-- /lc-block -->
</div><!-- /col -->
</div>
<div class="row mb-4 align-items-center">
<div class="col-lg-6 mb-4 mb-lg-0 order-lg-1">
<div class="lc-block text-center"><img class="img-fluid" src="https://cdn.livecanvas.com/media/svg/isometric/Startup_SVG.svg" width="400" height="400" loading="lazy"></div><!-- /lc-block -->
</div><!-- /col -->
<div class="col-lg-6 p-lg-6">
<div class="lc-block mb-5">
<div editable="rich">

<h2 class="display-6 fw-bold">Increase your Sales</h2>

<p class="lead"><br>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a lacus est. Etiam diam metus.</p>
</div>
</div><!-- /lc-block -->
<!-- /lc-block -->
<div class="lc-block">
<div class="d-inline-flex">
<div>
<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="text-primary" viewBox="0 0 16 16" lc-helper="svg-icon">
<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"></path>
</svg>
</div>

<div class="ms-3 align-self-center" editable="rich">
<p>Lorem ipsum dolor sit amet</p>
</div>
</div>
</div>
<div class="lc-block">
<div class="d-inline-flex">
<div>
<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="text-primary" viewBox="0 0 16 16" lc-helper="svg-icon">
<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"></path>
</svg>
</div>

<div class="ms-3 align-self-center" editable="rich">
<p>Consectetur adipiscing elit.</p>
</div>
</div>
</div>
<div class="lc-block">
<div class="d-inline-flex">
<div>
<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="text-primary" viewBox="0 0 16 16" lc-helper="svg-icon">
<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"></path>
</svg>
</div>

<div class="ms-3 align-self-center" editable="rich">
<p>Aenean vel nisi in ipsum congue</p>
</div>
</div>
</div><!-- /lc-block -->
</div><!-- /col -->
</div>

</div>
</div>
<div class="content" id="screen3" style="display: none;">
<div class="container py-5">
<div class="row mb-5">
<div class="col-md-12">
<div class="lc-block text-center">
<div editable="rich">
<h2 class="fw-bold">FAQ</h2>
</div>
</div>
<div class="lc-block text-center">
<div editable="rich">
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu<br>fugiat nulla pariatur excepteur sint occaecat.&nbsp;<br>Static Faq<br>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col-md-6">
<div class="lc-block mb-5">
<div editable="rich">
<p class="h4">Excepteur sint occaecat cupidatat non? </p>
<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>
</div>
<div class="lc-block mb-5">
<div editable="rich">
<p class="h4">Duis aute irure dolor in?</p>
<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>
</div>
<div class="lc-block mb-5">
<div editable="rich">
<p class="h4">Consequuntur magni dolores eos qui?</p>
<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>
</div>
</div>
<div class="col-md-6">
<div class="lc-block mb-5">
<div editable="rich">
<p class="h4">Duis aute irure dolor in?</p>
<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>
</div>
<div class="lc-block mb-5">
<div editable="rich">
<p class="h4">Consequuntur magni dolores eos qui?</p>
<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>
</div>
<div class="lc-block mb-5">
<div editable="rich">
<p class="h4">Excepteur sint occaecat cupidatat non? </p>
<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
</div>
</div>
</div>
</div>
</div>

</div>
</div>

<script>
function showScreen(screenId) {
document.querySelectorAll('.content').forEach(content => {
content.style.display = 'none';
});
document.getElementById(screenId).style.display = 'block';
}
</script>


<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
""",unsafe_allow_html=True)
