import streamlit as st
from init import init
init()
from showPages import atualizarEstado
from core import interfaceFrontEnd as iFE
import os
atualizarEstado(st.session_state["estado do usuario"])

stringMatricula = "Note que o seu número de matrícula informado deve coincidir com o número de matrícula da foto"

with st.form('cadastro'):
    matr = st.text_input("Matrícula", help=stringMatricula)
    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    imagem = st.file_uploader('Foto da sua carteirinha da UFMG', help=stringMatricula)
    submitted = st.form_submit_button("Submit")
    if submitted:
        if imagem is not None:
            if len(matr) != 0 and len(senha) != 0 and len(user) != 0:
                status = iFE().cadastraLogin(user, senha, 0, matr)
                if status == -1:
                    st.write("Houve um erro desconhecido.")
                elif status == -2:
                    st.write("Esse nome de usuário já está em uso.")
                elif status == -3:
                    st.write("Erro no cadastro da matricula.")
                else: 
                    st.write("nome de usuário", user)
                    st.write("senha", senha)
                    st.write("matrícula", matr)

                    id = iFE().verificaLogin(user, senha)

                    status = iFE().cadastraImagem(id, matr + " " + str(id), imagem.getvalue())

                    if status == -1:
                        st.write("Houve um erro desconhecido ao cadastrar Imagem.")
                    else:
                        st.write("Cadastro feito com sucesso.")

                    image = imagem.read()
                    img = st.image(image=image)
            else:
                st.write("Favor preencher todos os campos.")

        else:
            st.write("Favor adicionar uma imagem.")
