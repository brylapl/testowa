from bs4 import BeautifulSoup
import requests
import lxml
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
import funkcja

#------------------------ TABELA NA KURSY
		

win = [1,2,3]
dc = [1,2,3]
gole0 = [1,'0.5',2]
gole1 = [1,'1.5']
gole2 = [1,'2.5']
gole3 = [1,'3.5']
gole4 = [1,'4.5']
dnb = [1,'AH0',2]
bts = [1,'',2]
home0 = [1,'0.5',2]
home1 = [1,'1.5',2]
away0 = [1,'0.5',2]
away1 = [1,'1.5',2]
		

x = funkcja.glowna(win,dc,gole0,gole1,gole2,gole3,gole4,dnb,bts,home0,home1,away0,away1)
st.write(x)








