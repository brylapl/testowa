from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from flask import Flask, render_template
import streamlit.components.v1 as components


html_code = """
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hello World</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
<h1 class="mt-5 text-center">Color</h1>
</div>

<h1 class="h1 mt-5 text-center">Match Analyzer</h1>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<p class="text-center">ASDKLHASD
AJSD
ASDAS
ASDASD
ASDASD
</p>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""

components.html(html_code, height=400)

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


