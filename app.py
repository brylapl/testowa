from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from flask import Flask, render_template
import streamlit.components.v1 as components

# Przykładowy HTML
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        function resizeIframe(obj) {
            obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
        }
    </script>
</head>
<body>
<!-- Hero 6 - Bootstrap Brain Component -->
<section class="py-4 py-md-5">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <div class="container-fluid bsb-hero-6 bsb-overlay border border-dark" style="--bsb-overlay-opacity: 0.5; --bsb-overlay-bg-color: var(--bs-light-rgb); background-image: url('./assets/img/hero-img-1.webp');">
          <div class="row justify-content-md-center align-items-center">
            <div class="col-12 col-md-11 col-xl-10">
              <h2 class="display-1 text-center text-md-start text-shadow-head fw-bold mb-4">Welcome to Presta</h2>
              <p class="lead text-center text-md-start text-shadow-body mb-5 d-flex justify-content-sm-center justify-content-md-start">
                <span class="col-12 col-sm-10 col-md-8 col-xxl-7">Where every squeak, every rattle, and every wobble finds its solution, ensuring your ride is always smooth and worry-free.</span>
              </p>
              <div class="d-grid gap-2 d-sm-flex justify-content-sm-center justify-content-md-start">
                <a href="#!" class="btn bsb-btn-2xl btn-outline-dark">Explore More</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</body>
</html>
'''

# Wyświetlanie HTML w Streamlit
st.components.v1.html(html_content, height=5000)
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


