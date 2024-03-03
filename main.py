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
dc = [1.20,1.35,1.89]
gole0 = [1.55,'0.5',2.8]
gole1 = [1,'1.5',3]
gole2 = [5,'2.5',4]
gole3 = [6,'3.5',8]
gole4 = [1,'4.5',2]
dnb = [1.50,'AH0',2.40]
bts = [2.0,1.90]
home0 = [1,'0.5',2]
home1 = [1,'1.5',3]
away0 = [4,'0.5',6]
away1 = [5,'1.5',7]
		

x = funkcja.glowna(win,dc,gole0,gole1,gole2,gole3,gole4,dnb,bts,home0,home1,away0,away1)
st.write(x)








