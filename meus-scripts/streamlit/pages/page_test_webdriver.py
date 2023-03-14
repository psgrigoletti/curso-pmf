import streamlit as st
from time import sleep
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
    
"""
## Web scraping on Streamlit Cloud with Selenium
[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)
This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.
Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

@st.experimental_singleton
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()

with st.echo():
    url = f'https://sistemaswebb3-listados.b3.com.br/indexPage/day/{"IBOV".upper()}?language=pt-br'
    driver.get(url)
    driver.find_element(By.ID, 'segment').send_keys("Setor de Atuação")
    sleep(8)

    driver.find_element(By.LINK_TEXT, "Download").click()
    sleep(8)

    caminho = os.getcwd()
    arquivos = os.listdir(caminho)
    arquivos = [f for f in arquivos if f[-3:] == 'csv' and "IBOV".upper() in f]
    
st.dataframe(pd.read_csv(arquivos[0], sep=';', encoding='ISO-8859-1', skipfooter=2, 
                         engine="python", thousands='.', decimal=',', header=1, index_col=False))