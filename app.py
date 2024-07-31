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
    <h1>Hello, World!</h1>
    <p>This is a dynamic height example.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis porttitor sapien at mi malesuada laoreet. Sed vel porttitor libero, tempus cursus dui. In gravida sagittis malesuada. Vivamus nisl magna, feugiat id ante suscipit, imperdiet dignissim ipsum. Suspendisse dolor nulla, mattis at turpis at, sagittis tristique enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus, nibh eget condimentum blandit, enim massa vulputate metus, eget placerat dolor turpis quis nibh. Integer congue enim vel massa luctus, vitae euismod ex efficitur. Aenean lacus purus, dapibus vel nisi eget, dictum bibendum ante. Sed id diam in risus gravida aliquet ac at enim. Phasellus vel nisi ac felis congue viverra. Phasellus in arcu hendrerit, sollicitudin erat vel, rhoncus quam.

Nam erat neque, scelerisque a erat eget, aliquet pretium velit. Aliquam vulputate libero id massa iaculis placerat. Nullam pulvinar vitae nisi auctor tincidunt. Donec tortor massa, dictum a quam eget, semper dictum sapien. Nam elementum, enim a venenatis fermentum, dolor dui suscipit felis, placerat tempus est mauris sit amet leo. Sed faucibus nulla eu tortor consequat blandit. Phasellus ultricies non lectus vel tincidunt. Duis eu tempus metus.

Morbi nisl ex, aliquam in scelerisque tincidunt, ultricies a tortor. Aliquam eu consequat justo. Aenean hendrerit quis erat et maximus. Ut non vehicula lacus. Nam porta eros ut mi tempor sodales. Proin nec malesuada libero. Suspendisse viverra eleifend tempus. Nunc consequat enim massa, sit amet accumsan lacus ultricies facilisis. Nulla efficitur ex dictum imperdiet maximus. Ut id leo feugiat, aliquam odio non, condimentum felis. Fusce tristique lectus eget fermentum cursus. Duis pharetra justo sed semper sollicitudin. Cras varius dapibus ante at malesuada. Vivamus eleifend eu mi et tincidunt. Praesent lectus diam, dignissim ac justo ac, egestas volutpat velit.

Ut tincidunt odio non lectus condimentum viverra. Suspendisse sed orci ac nulla fringilla vestibulum vitae nec est. Nulla lectus arcu, finibus et aliquet ac, tincidunt ac dolor. In magna mauris, imperdiet commodo massa vitae, aliquet lobortis leo. Nulla facilisi. Maecenas eget viverra augue. Aenean tincidunt gravida lobortis. Vivamus eu massa semper diam egestas ullamcorper non eget lacus. Phasellus sit amet leo ac felis pharetra finibus vitae non nunc. Maecenas vel interdum tortor. Aenean fringilla lacinia leo sed lobortis. Donec ac libero mauris. Mauris a nibh leo. Fusce blandit at velit a vulputate. Ut id nibh ac leo sollicitudin ultrices. Praesent et nisl et mauris ornare bibendum.

Donec dictum justo non dui aliquam, sit amet pretium magna tincidunt. Sed dui justo, faucibus in pulvinar sit amet, ullamcorper facilisis nunc. Curabitur semper bibendum mauris. Duis eu semper massa. In turpis ipsum, tincidunt nec dui vitae, varius pharetra lacus. Donec elit turpis, mollis eget justo id, ullamcorper semper quam. Proin non sagittis eros. Proin sed magna at enim viverra feugiat id sed orci. Nulla ac porta libero. Morbi et congue urna. Maecenas suscipit, elit nec dapibus tempor, mi nibh interdum elit, eget tempor nulla odio vel magna. Mauris condimentum aliquet felis, quis semper enim laoreet vel. Sed consequat, felis at consequat pellentesque, elit lectus pellentesque dolor, non suscipit est orci ut sapien.</p>
</body>
</html>
'''

# Wyświetlanie HTML w Streamlit
st.components.v1.html(html_content, height=500)
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


