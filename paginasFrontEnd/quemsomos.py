import streamlit as st
from init import init
init()
from showPages import atualizarEstado
atualizarEstado(st.session_state["estado do usuario"])

st.write("# Quem somos?")
st.write("O DCC-Rating é um site de review de matérias do Departamento de Ciência da Computação da UFMG.")
st.write("Ele foi feito para a disciplina de Prática em Desenvolvimento de Software pelos alunos Kael, Lucas, Wilgnert e Astris.")