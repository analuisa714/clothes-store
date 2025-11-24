import streamlit as st
from google.cloud import firestore


html_code = '''
<h1 style='color: #5b1f00'> Cadastro de produto </h1>
'''

st.markdown(html_code, unsafe_allow_html=True)
st.markdown("---")


html_code = '''
<h4 style='color: #cd966c'> Formulário para cadastrar um novo item no estoque </h4>
'''

st.markdown(html_code, unsafe_allow_html=True)

db = firestore.Client.from_service_account_json("firebase.json")

tam_opcoes = ['PP', 'P', 'M', 'G', 'XG']
categoria_opcoes = ['Blusa - manga curta', 'Blusa - Manga longa', 'T-Shirt', 'Cropped', 'Saia', 'Shorts', 'Macacão', 'Macaquinho', 'Calça', 'Vestido', '']

col1, col2, col3 = st.columns([1, 5, 1])

with col2: 
    with st.form("formCadProd"):
        id_peca = st.text_input("ID: ", placeholder="Digite um identificador para a peça...")
        categoria = st.selectbox("Categoria:", categoria_opcoes, placeholder= "Escolha a categoria da peça...", index=None)
        tam = st.selectbox("Tamanho: ", tam_opcoes, placeholder="Escolha o tamanho da peça...", index=None)
        cor = st.text_input("Cor: ", placeholder="Digite a cor da peça...")
        qtdade_min = st.number_input("Quantidade mínima: ", step=1)
        qtdade = st.number_input("Quantidade total em estoque: ", step=1)
        preco = st.number_input("Preço: ", placeholder="Digite o preço desse produto em reais...", min_value=0.0, step=0.01)
        # img = st.file_uploader("Anexe um foto da peça aqui")
        btn_cad_prod = st.form_submit_button("Cadastrar", use_container_width=True)

        if btn_cad_prod:
            if not (categoria and id and tam and cor and qtdade_min and qtdade and preco):
                st.error("Preencha todos os campos!")
            else:
                novo_prod = db.collection("produto").document(id_peca)
                novo_prod.set(
                    {
                        "categoria": categoria,
                        "cor": cor,
                        "preco": preco,
                        "qtdade_min": qtdade_min,
                        "qtdade": qtdade,
                        "tamanho": tam
                    }
                )
                st.success("Produto cadastrado com sucesso!")
