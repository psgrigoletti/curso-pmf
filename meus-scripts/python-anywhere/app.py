# https://www.alura.com.br/artigos/ambientes-virtuais-em-python

from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title="Dashboard Margem Líquida",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Tesouro Direto', 'Relatório Focus'], 
                         iconName=['dashboard', 'money', ], default_choice=0)

if tabs =='Tesouro Direto':
    st.title("Tesouro direto")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Relatório Focus':
    st.title("Relatório Focus")
    st.write('Name of option is {}'.format(tabs))