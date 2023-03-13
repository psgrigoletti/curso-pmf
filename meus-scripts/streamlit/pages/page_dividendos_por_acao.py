import streamlit as st
import datetime
from libs.dividendos import Dividendos 
import logging

st.set_page_config(layout="wide")

from st_pages import add_page_title

st.markdown("# Dividendos")

add_page_title()

@st.cache_data
def retornar_dados(ticker, data_inicial, data_final):
    logging.log(logging.INFO, f"Buscando histórico de {ticker} entre {data_inicial} e {data_final}")
    d = Dividendos()
    d.setar_chave_carteira_global(st.secrets["carteira_global"]["x_api_key"])
    dados = d.retornar_dados(ticker, data_inicial, data_final)
    return dados

col1, col2, col3 = st.columns([1,1,1])

ticker = col1.text_input('Informe o ticker:', "WEGE3")
data_inicial = col2.date_input(
    "Data inicial:",
    datetime.date(2018, 1, 1))

data_final = col3.date_input(
    "Data final:",
    datetime.date(2023, 3, 12))

if st.button("Buscar informações", help="Buscar informações"):
    dados = retornar_dados(ticker, data_inicial, data_final)
    graficos, tabela = st.tabs(["Gráficos", "Dados"])
        
    with tabela:
        st.dataframe(dados, width=0, height=0, use_container_width=True)

    with graficos:
        d = Dividendos()
        d.setar_chave_carteira_global(st.secrets["carteira_global"]["x_api_key"])       
        st.markdown(f"## {ticker} - Evolução dos Dividendos e Dividend Yield")
        st.plotly_chart(d.retornar_grafico_evolucao(ticker, dados), use_container_width=True)
        #st.bar_chart(dados['Dividends'], width=0, height=0, use_container_width=True)
        
        st.markdown(f"## {ticker} - Tendência dos Dividendos e Dividend Yield")
        #st.line_chart(dados['Dividends'].rolling(10).mean(), width=0, height=0, use_container_width=True)
        st.plotly_chart(d.retornar_grafico_tendencia(ticker, dados), use_container_width=True)

        st.markdown(f"## {ticker} - Dividendos pagos por mês")
        st.markdown(f"Soma dos dividendos pagos, em R$, agrupados por mês.")
        st.markdown(f"Considerando o período entre {data_inicial} e {data_final}.")
        #div_mes = dados.groupby(['NomeMês'])[['NomeMês', 'Mês', 'Dividends']].sum(numeric_only=True).head().sort_values('Mês')['Dividends']
        #st.bar_chart(div_mes, width=0, height=0, use_container_width=True)
        st.plotly_chart(d.retornar_grafico_mensal(ticker, dados), use_container_width=True)

        st.markdown(f"## {ticker} - Dividendos pagos por ano")
        st.markdown(f"Soma dos dividendos pagos, em R$, agrupados por ano.") 
        st.markdown(f"Considerando o período entre {data_inicial} e {data_final}.")
        #st.bar_chart(dados.groupby(['Ano'])['Dividends'].sum(numeric_only=True), width=0, height=0, use_container_width=True)
        st.plotly_chart(d.retornar_grafico_anual(ticker, dados), use_container_width=True)

        st.markdown(f"## {ticker} - Número de vezes que pagou dividendos por ano")
        st.markdown(f"Considerando o período entre {data_inicial} e {data_final}.")
        st.plotly_chart(d.retornar_grafico_quantidade_pagamentos_anual(ticker, dados), use_container_width=True)  
        
        # st.markdown(f"## Dividend Yield de {ticker}")
        # dividend_yield = dados['DY'] # dividir pelo último valor em cada ano (multiplicar por 100)
        # st.bar_chart(dividend_yield, width=0, height=0, use_container_width=True)

