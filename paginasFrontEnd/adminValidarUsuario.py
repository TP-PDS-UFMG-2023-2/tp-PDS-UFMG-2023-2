import streamlit as st
from init import init
init()
from showPages import atualizarEstado
from core import interfaceFrontEnd as iFE
atualizarEstado(st.session_state["estado do usuario"])
if st.session_state["estado do usuario"] != "admin":
    st.warning("Você não tem permissão para acessar essa página, volte ao login")
    st.stop()


pending_users = iFE().getUsersPendentes()

user_id_pendentes = [x[0] for x in pending_users]
iFE().aceitaUsuario(17)

lista_pendentes = ["Usuário pendente ID: " + str(x) for x in user_id_pendentes]

selected = st.selectbox("Selecione usuário pendente",
                                           lista_pendentes)
if selected == None:
    st.stop()

i = lista_pendentes.index(selected)
user_pendente = iFE().retornaInfosUsuario(user_id_pendentes[i])

st.write("UserID: " + str(user_pendente[0]))
st.write("Matrícula: " + str(user_pendente[2]))
st.write("Foto: ")
status = iFE().salvaImagem("temp/matricula.png", user_pendente[0])
if status == 0:
    st.image("temp/matricula.png")

colunas = st.columns(5)

with colunas[0]: 
    aceitar = st.button("Aceitar")
    if aceitar:
        iFE().aceitaUsuario(user_pendente[0])
        st.rerun()


with colunas[4]:
    recusar = st.button("Recusar")
    if recusar:
        iFE().recusaUsuario(user_pendente[0])
        st.rerun()
