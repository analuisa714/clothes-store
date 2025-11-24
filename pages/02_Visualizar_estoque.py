import streamlit as st
import pandas as pd
from google.cloud import firestore

st.set_page_config(layout="wide")

html_code = '''
<h1 style='color: #5b1f00'> Produtos cadastrados </h1>
'''

st.markdown(html_code, unsafe_allow_html=True)
st.markdown("---")

db = firestore.Client.from_service_account_json("firebase.json")

prods = db.collection("produto").stream()

lista_produtos = []
for prod in prods:
    dados = prod.to_dict()
    dados["id"] = prod.id  
    lista_produtos.append(dados)

if lista_produtos:

    df = pd.DataFrame(lista_produtos)

    df = df.rename(columns={
        "id": "ID",
        "categoria": "Categoria",
        "tamanho": "Tamanho",
        "cor": "Cor",
        "qtdade_min": "Qtd mín",
        "qtdade": "Qtd",
        "preco": "Preço"
    })

    colunas_ordenadas = ["ID", "Categoria", "Tamanho", "Cor", "Qtd mín", "Qtd", "Preço"]
    df = df[colunas_ordenadas]

    st.markdown("""
        <style>
        df {
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)


    st.dataframe(df, use_container_width=True, hide_index=True, width="stretch")

else:
    st.info("Nenhum produto cadastrado ainda.")
