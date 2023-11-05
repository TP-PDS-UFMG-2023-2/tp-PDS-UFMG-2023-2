import streamlit as st
from init import init
init()
from showPages import atualizarEstado
from core import interfaceFrontEnd as iFE
atualizarEstado(st.session_state["estado do usuario"])
if st.session_state["estado do usuario"] != "logado":
    st.warning("Você não tem permissão para acessar essa página, volte ao login")
    st.stop()


usuario = iFE().retornaInfosUsuario(st.session_state["user_id"])
permlvl = usuario[1] 
st.markdown(f'**Nome:** {st.session_state.get("user_name")}')
st.markdown(f'**Matrícula:** {st.session_state.get("user_matr")}')
user_status = ""
if permlvl == 0:
    user_status = "Pendente..."
elif permlvl == 1:
    user_status = "Aprovado!"
elif permlvl == -1:
    user_status = "Negado."
elif permlvl == 2:
    user_status = "Admin"

st.markdown(f'**Status do perfil:** {user_status}')

st.write('Sua foto')
status = iFE().salvaImagem("temp/matricula.png", int(st.session_state["user_id"]))
if status == -1:
    st.write("Erro desconhecido...")
elif status == -2 or status == -3:
    st.write("Imagem não encontrada.")
elif status == 0:
    st.image("temp/matricula.png")

