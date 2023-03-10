# https://www.alura.com.br/artigos/ambientes-virtuais-em-python

import streamlit as st
import yfinance as yf

st.header('Dashboard Margem Líquida')
st.text("Gráfico PETZ.SA")

df = yf.download("PETZ3.SA")
st.line_chart(df)
