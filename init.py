import streamlit as st
from showPages import showPagesAll, atualizarEstado


def init():
    if "init" not in st.session_state:
        st.session_state["init"] = True
        if "estado do usuario" not in st.session_state:
            st.session_state["estado do usuario"] = "deslogado"
        showPagesAll()
        atualizarEstado(st.session_state["estado do usuario"])
