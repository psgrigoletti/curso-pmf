# https://www.alura.com.br/artigos/ambientes-virtuais-em-python

from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import tesouro_direto as td
from datetime import datetime

@st.cache_data
def retorna_dados_td(data):
    o = td.TesouroDireto()
    o.atualizar_graficos()
    return o

st.set_page_config(
    page_title="Dashboard Margem Líquida",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Tesouro Direto', 'Relatório Focus'], 
                         iconName=['dashboard', 'money', ], default_choice=0)

if tabs =='Tesouro Direto':
    objeto = retorna_dados_td(datetime.today().today().strftime('%d/%m/%Y'))
    st.button("Atualizar", help="Atualizar gŕaficos", on_click=retorna_dados_td(datetime.today().today().strftime('%d/%m/%Y')))
    st.title("Tesouro direto")
    st.write("Tesouro SELIC")
    st.plotly_chart(objeto.retornar_grafico_precos_tesouro_selic(), use_container_width=True)
    st.plotly_chart(objeto.retornar_grafico_taxas_tesouro_selic(), use_container_width=True)
    st.write("Tesouro IPCA+")
    st.plotly_chart(objeto.retornar_grafico_precos_tesouro_ipca(), use_container_width=True)
    st.plotly_chart(objeto.retornar_grafico_taxas_tesouro_ipca(), use_container_width=True)
    st.write("Tesouro Préfixado")
    st.plotly_chart(objeto.retornar_grafico_precos_tesouro_pre(), use_container_width=True)
    st.plotly_chart(objeto.retornar_grafico_taxas_tesouro_pre(), use_container_width=True)  
    
elif tabs == 'Relatório Focus':
    st.title("Relatório Focus")
    st.write('Name of option is {}'.format(tabs))