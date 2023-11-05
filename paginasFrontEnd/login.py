import streamlit as st
from init import init
init()
from showPages import atualizarEstado
from core import interfaceFrontEnd as iFE
atualizarEstado(st.session_state["estado do usuario"])

from time import sleep

colunas = st.columns(2)

with colunas[0]:
    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Logar"):
        status = iFE().verificaLogin(user, senha)

        if status == -1:
            st.session_state["estado do usuario"] = "deslogado"
            st.session_state["user_id"] = -1
            st.session_state["user_permLvl"] = -2
            st.session_state["user_matr"] = -1
            atualizarEstado(st.session_state["estado do usuario"])
            st.write("Login ou senha incorretos.")
            sleep(1) # Não foi minha ideia.
            st.rerun()
        else:
            st.session_state["user_name"] = user
            usuario = iFE().retornaInfosUsuario(status)

            st.session_state["user_id"] = usuario[0]
            st.session_state["user_permLvl"] = usuario[1]
            st.session_state["user_matr"] = usuario[2]
            if st.session_state["user_permLvl"] == 2:
                st.session_state["estado do usuario"] = "admin"
            else: 
                st.session_state["estado do usuario"] = "logado"
            atualizarEstado(st.session_state["estado do usuario"])
            st.write("Logado com sucesso")
            sleep(1) # Não foi minha ideia.
            st.rerun()
