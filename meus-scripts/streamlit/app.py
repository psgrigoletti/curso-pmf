# https://www.alura.com.br/artigos/ambientes-virtuais-em-python

import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


st.set_page_config(
    page_title="Dashboard Margem Líquida",
    layout="wide",
)

add_page_title()

st.markdown("# Página Principal")
st.sidebar.markdown("# Página Principal")

# emojis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
show_pages(
    [
        # Page("pages/page_inicial.py", "Inicial", ":beginner:"),        
        Section(name="Dividendos", icon=":wavy_dash:"),
        Page(st.secrets["pasta_ajustada"] + "pages/page_dividendos_por_acao.py", "Por ação", ":moneybag:"),
        Page(st.secrets["pasta_ajustada"] + "pages/page_dividendos_maiores_pagadores.py", "Maiores pagadores", ":moneybag:"),
        Section(name="Outros", icon=":mate_drink:"),        
        Page(st.secrets["pasta_ajustada"] + "pages/page_analise_fundamentalista.py", "Análise Fundamentalista", ":bank:"),
        Page(st.secrets["pasta_ajustada"] + "pages/page_relatorio_focus.py", "Relatório Focus", ":newspaper:"),
        Page(st.secrets["pasta_ajustada"] + "pages/page_tesouro_direto.py", "Tesouro Direto", ":flag-br:"),
    ]
)