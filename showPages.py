import streamlit as st
from st_pages import Page, show_pages, hide_pages


def showPagesAll():
    show_pages([
        Page("./dccReview.py", "DCC Rating"),
        Page("./paginasFrontEnd/login.py", "Login"),
        Page("./paginasFrontEnd/cadastro.py", "Cadastro"),
        Page("./paginasFrontEnd/meuPerfil.py", "Meu perfil"),
        Page("./paginasFrontEnd/materias.py", "Matérias"),
        Page("./paginasFrontEnd/fazerReviews.py", "Fazer review"),
        Page("./paginasFrontEnd/adminValidarUsuario.py", "[Admin] Validar usuário"),
        Page("./paginasFrontEnd/adminCriarRemoverMateria.py", "[Admin] Criar e remover matérias"),
        Page("./paginasFrontEnd/quemsomos.py", "Quem Somos?"),
        Page("./paginasFrontEnd/faq.py", "FAQ")
    ])


def pagDeslogado():
    #showPagesAll()
    #show_pages([
    #    Page("./dccReview.py", "DCC Review"),
    #    Page("./paginasFrontEnd/login.py", "Login"),
    #    Page("./paginasFrontEnd/cadastro.py", "Cadastro"),
    #    Page("./paginasFrontEnd/quemsomos.py", "Quem somos?"),
    #    Page("./paginasFrontEnd/faq.py", "FAQ")
    #])
    hide_pages(["Meu perfil", "Matérias", "Fazer review", "[Admin] Validar usuário", "[Admin] Criar e remover matérias"])


def pagLogado():
    #showPagesAll()
    #show_pages([
    #    Page("./dccReview.py", "DCC Review"),
    #    Page("./paginasFrontEnd/meuPerfil.py", "Meu perfil"),
    #    Page("./paginasFrontEnd/materias.py", "Matérias"),
    #    Page("./paginasFrontEnd/fazerReviews.py", "Fazer review"),
    #    Page("./paginasFrontEnd/quemsomos.py", "Quem somos?"),
    #    Page("./paginasFrontEnd/faq.py", "FAQ")
    #])
    hide_pages(["Login", "Cadastro", "[Admin] Validar usuário", "[Admin] Criar e remover matérias"])

def pagAdmin():
    #showPagesAll()
    #show_pages([
    #    Page("./dccReview.py", "DCC Review"),
    #    Page("./paginasFrontEnd/adminValidarUsuario.py", "[Admin] Validar usuário"),
    #    Page("./paginasFrontEnd/adminCriarRemoverMateria.py", "[Admin] Criar e remover matérias"),
    #    Page("./paginasFrontEnd/quemsomos.py", "Quem somos?"),
    #    Page("./paginasFrontEnd/faq.py", "FAQ")
    #])
    hide_pages(["Login", "Cadastro", "Meu perfil", "Matérias", "Fazer review"])

def atualizarEstado(estado:str):
    #st.rerun()
    if(estado == "deslogado"):
        pagDeslogado()
    elif(estado == "logado"):
        pagLogado()
    elif(estado == "admin"):
        pagAdmin()
