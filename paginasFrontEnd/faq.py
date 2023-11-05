import streamlit as st
from init import init
init()
from showPages import atualizarEstado
atualizarEstado(st.session_state["estado do usuario"])


st.write("# Frequently Asked Questions (FAQ):")

st.write("**Q: Como posso me inscrever no DCC-Review?**")
st.write("A: basta ir no \"Cadastro\" e se inscrever com uma foto da carteirinha, um nome de usuário e senha.")

st.write("**Q: Posso falar o que quiser no review da matéria?**")
st.write("A: Use do bom senso! Insultos pessoais e derrogatórios não serão aceitos. Tente ser formal sempre que possível.")

st.write("**Q: Ainda não vi a materia X no site. Como faço para fazer um review dela?**")
st.write("A: Contate um dos administradores. Apenas eles são capazes de adicionar matérias novas.")

