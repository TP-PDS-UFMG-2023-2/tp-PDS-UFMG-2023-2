import streamlit as st
from st_pages import Page, show_pages, hide_pages


def showPagesAll():
    show_pages([
        Page("./dccReview.py", "DCC Rating"),
        Page("./paginasFrontEnd/materias.py", "Matérias"),
        Page("./paginasFrontEnd/fazerReviews.py", "Fazer review")
    ])


def pagDeslogado():
    #showPagesAll()
    hide_pages(["Matérias", "Fazer review"])


def pagLogado():
    #showPagesAll()
    hide_pages([])

def pagAdmin():
    #showPagesAll() 
    hide_pages(["Matérias", "Fazer review"])

def atualizarEstado(estado:str):
    #st.rerun()
    if(estado == "deslogado"):
        pagDeslogado()
    elif(estado == "logado"):
        pagLogado()
    elif(estado == "admin"):
        pagAdmin()
