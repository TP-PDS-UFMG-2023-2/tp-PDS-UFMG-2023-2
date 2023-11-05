import streamlit as st
from init import init
init()
from showPages import atualizarEstado
atualizarEstado(st.session_state["estado do usuario"])


if st.button("deslogado"):
    st.session_state["estado do usuario"] = "deslogado"
    #st.experimental_rerun()
    st.rerun()

if st.button("logado"):
    st.session_state["estado do usuario"] = "logado"
    #st.experimental_rerun()
    st.rerun()

if st.button("admin"):
    st.session_state["estado do usuario"] = "admin"
    #st.experimental_rerun()
    st.rerun()

init()
atualizarEstado(st.session_state["estado do usuario"])

# Página DCC-Review
from PIL import Image
title_image = Image.open("assets/DCC_Rating.png")

st.image(title_image, width = 750)
