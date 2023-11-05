import streamlit as st
from init import init
init()
from showPages import atualizarEstado
atualizarEstado(st.session_state["estado do usuario"])


# Página DCC-Review
from PIL import Image
title_image = Image.open("assets/DCC_Rating.png")

st.image(title_image, width = 750)


if st.button("Deslogar"):
    st.session_state["estado do usuario"] = "deslogado"
    #st.experimental_rerun()
    st.rerun()

init()
atualizarEstado(st.session_state["estado do usuario"])