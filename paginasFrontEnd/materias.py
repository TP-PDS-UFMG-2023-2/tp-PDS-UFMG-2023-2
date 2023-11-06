import streamlit as st
from init import init
init()
from showPages import atualizarEstado
from core import interfaceFrontEnd as iFE
atualizarEstado(st.session_state["estado do usuario"])
if st.session_state["estado do usuario"] != "logado":
    st.warning("Você não tem permissão para acessar essa página, volte ao login")
    st.stop()

from streamlit_star_rating import st_star_rating

#listaMaterias = ["Mat", "port", "red"]

materias = iFE().getListaMaterias()
id_materias = [x[0] for x in materias]
nome_materias = [x[1] + " - " + x[3] + " - " + x[2] for x in materias]

listaMateriasSelecionadas = st.multiselect("Selecione as matérias",
                                           nome_materias)

if(len(listaMateriasSelecionadas) == 0):
    st.stop()

listaAbas = st.tabs(listaMateriasSelecionadas)

for i in range(len(listaMateriasSelecionadas)):
    with listaAbas[i]:
        st.write("Você está na aba da matéria %s"%listaMateriasSelecionadas[i])

        reviews = iFE().getReviewMateria(id_materias[i])

        total = 0
        for review in reviews:
            total += int(review[3])
        if len(reviews) > 0:
            st.write("Média: %.3f"%(total / len(reviews)))

        for review in reviews: 
            with st.expander("Review %d da materia %s"%(review[0], listaMateriasSelecionadas[i])):
                st.write(review[4])
                st_star_rating(size=40, defaultValue=review[3], maxValue=5, read_only=True, key="%s%d"%(nome_materias[i], review[0]), label="")


