import streamlit as st
import pandas as pd
from google.cloud import firestore
from streamlit_option_menu import option_menu

html_code = '''
<h1 style='color: #5b1f00'> Gerenciador de estoque </h1>
'''

st.markdown(html_code, unsafe_allow_html=True)
st.markdown("---")

optionMenu = option_menu(
    menu_title="O que você deseja fazer?",
    options=['Excluir um item', 'Alterar informações de um item'],
    icons=['flashlight', 'ghost'],
    menu_icon='cast',
    default_index=0, 
    orientation='horizontal',
    styles = {
        "container": {"padding": "0!important", "background-color":"#fafafa"},
        "nav-link": {
            "font-size": "25px",
        "font-align": "left",
        "margin": "0px",
        "--hover-color": "#eee",
        "color": "black"
        },
        "nav-link-selected": {"background-color": "#5b1f00", "color": "white"}
    }
)

if optionMenu == 'Excluir um item':
    with st.form('formExcluir'):
        id = st.text_input('ID: ', placeholder='Digite aqui o ID do produto...')

tam_opcoes = ['PP', 'P', 'M', 'G', 'XG']
categoria_opcoes = ['Blusa - manga curta', 'Blusa - Manga longa', 'T-Shirt', 'Cropped', 'Saia', 'Shorts', 'Macacão', 'Macaquinho', 'Calça', 'Vestido', '']
info_opcoes = ['Tamanho', 'Cor', 'Quantidade mínima', 'Preço']

if optionMenu == 'Alterar informações de um item':
    with st.form('formAlterar'):
        id = st.text_input('ID: ', placeholder='Digite aqui o ID do produto...')
        infoSelecionada = st.multiselect("Selecione quais informações você quer alterar do produto:", info_opcoes)
        st.form_submit_button("Avançar")
        for opcao in infoSelecionada:
            match opcao:
                case 'Tamanho':
                    tam = st.selectbox("Tamanho: ", tam_opcoes, placeholder="Escolha o tamanho da peça...", index=None)
                case 'Cor':
                    cor = st.text_input("Cor: ", placeholder="Digite a cor da peça...")
                case 'Quantidade mínima':
                    qtdade_min = st.number_input("Quantidade mínima: ", step=1)
                case 'Preço':
                    preco = st.number_input("Preço: ", placeholder="Digite o preço desse produto em reais...", min_value=0.0, step=0.01)
    