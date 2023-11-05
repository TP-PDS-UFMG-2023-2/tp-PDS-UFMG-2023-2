import streamlit as st
from init import init
init()
from showPages import atualizarEstado
from core import interfaceFrontEnd as iFE
atualizarEstado(st.session_state["estado do usuario"])
if st.session_state["estado do usuario"] != "admin":
    st.warning("Você não tem permissão para acessar essa página, volte ao login")
    st.stop()


colunas = st.columns(3)

with colunas[0]:
    codigoMateria = st.text_input("Código da matéria.")
    nomeMateria = st.text_input("Nome da matéria.")
    profMateria = st.text_input("Professor da matéria.")
    
    if st.button("Criar"):
        if len(codigoMateria) == 0 or len(nomeMateria) == 0 or len(profMateria) == 0:
            st.write("Favor preencher todos os campos.")
        else:
            status = iFE().cadastraMateria(codigoMateria, nomeMateria, profMateria)
            if status == 0:
                st.write("Materia criada com sucesso!")
            else:
                st.write("Houve um erro. Confirme que essa matéria ainda não existe.")
            
with colunas[2]:
    materias = iFE().getListaMaterias()
    nome_materias = [str(x[0]) + " " + x[1] + "-" + x[2] + " " + x[3] for x in materias]
    print(materias)
    materia_selecionada = st.selectbox("Selecione matéria para remover.", nome_materias)



    if st.button("Remover"):
        i = nome_materias.index(materia_selecionada)
        idMateria = materias[i][0]
        status = iFE().removeMateria(idMateria)
        if status == 0:
            st.write("Materia deletada com sucesso!")
        else:
            st.write("Houve um erro. Tente novamente ou verifique o código.")

