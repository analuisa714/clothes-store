import streamlit as st

st.set_page_config(layout="wide")


html_code = '''
<h1 style='color: #5b1f00'> Pegasus • Marketplace ®</h1>
<h2 style='color: #cd966c'> Loja de roupas virtual 👜 </h2>
'''

st.markdown(html_code, unsafe_allow_html=True)
st.markdown("---")

st.write("Seja bem-vindo(a) a nossa plataforma online para gerenciar o estoque de nossa loja de roupas!")
# incluir animação aqui
st.image("/workspaces/clothes-store/img/pag_index.jpg", use_container_width=True)
