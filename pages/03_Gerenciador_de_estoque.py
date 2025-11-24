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
    options=['🗑️ Excluir um item', '✍🏻 Alterar informações de um item'],
    menu_icon='none',
    default_index=0, 
    orientation='horizontal',
    styles = {
        "container": {"padding": "0!important", "background-color":"#ffd7ab", "font": "'Josefin Sans':https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&display=swap"},
        "nav-link": {
            "font-size": "25px",
        "font-align": "center",
        "text-align": "center",
        "margin": "0px",
        "--hover-color": "#e1bd96c8",
        "color": "black"
        },
        "nav-link-selected": {"background-color": "#d5b491ff", "color": "white"}
    }
)

col1, col2, col3 = st.columns([1, 5, 1])
db = firestore.Client.from_service_account_json("firebase.json")

with col2: 
    if optionMenu == '🗑️ Excluir um item':
        with st.form('formExcluir'):
            id = st.text_input('ID: ', placeholder='Digite aqui o ID do produto...')
            btn_excluir = st.form_submit_button("Excluir", use_container_width=True)
            if btn_excluir:
                if not id:
                    st.error("Informe um ID válido")
                else:
                    db.collection("produto").document(id).delete()
                    st.success('Produto excluído com sucesso')

tam_opcoes = ['PP', 'P', 'M', 'G', 'XG']
info_opcoes = ['Tamanho', 'Cor', 'Quantidade mínima', 'Preço']


with col2: 
    if "mostrar_form_alterar" not in st.session_state:
        st.session_state.mostrar_form_alterar = False

    if optionMenu == '✍🏻 Alterar informações de um item':

        with st.form('formEscolher'):
            id = st.text_input('ID: ', placeholder='Digite aqui o ID do produto...')
            infoSelecionada = st.multiselect("Selecione quais dados você quer alterar do produto:", info_opcoes, placeholder="Escolha uma opção...")
            btn_avancar = st.form_submit_button("Avançar", use_container_width=True)

        if btn_avancar:
            if id and infoSelecionada:
                st.session_state.id = id
                st.session_state.infoSelecionada = infoSelecionada
                st.session_state.mostrar_form_alterar = True
            else:
                st.error("Preencha todos os campos!")

        if st.session_state.mostrar_form_alterar:
            st.markdown("<h4 style='text-align: center;'>Informe os novos dados ↓</h4>", unsafe_allow_html=True)

            with st.form('formAlterar'):

                valores = {}

                for opcao in st.session_state.infoSelecionada:

                    match opcao:
                        case "Tamanho": valores["tamanho"] = st.selectbox("Tamanho: ", tam_opcoes, placeholder="Escolha o tamanho da peça...", index=None)
                        case "Cor": valores["cor"] = st.text_input("Cor: ", placeholder="Digite a cor da peça...")
                        case "Quantidade mínima": valores["qtdade_min"] = st.number_input( "Quantidade mínima: ", step=1)
                        case "Preço": valores["preco"] = st.number_input("Preço: ", placeholder="Digite o preço desse produto em reais...", min_value=0.0, step=0.01)

                btn_alterar = st.form_submit_button("Alterar", use_container_width=True)

                if btn_alterar:

                    db.collection("produto").document(st.session_state.id).update(valores)
                    st.success("Produto alterado com sucesso! ")

                    # reseta estado do forms
                    st.session_state.mostrar_form_alterar = False

