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

permLvl = iFE().retornaInfosUsuario(st.session_state["user_id"])[1]

if permLvl != 1 and permLvl != 2:
    st.write("Sua conta deve ser aprovada para fazer reviews.")
elif permLvl == 1 or permLvl == 2:
    materias = iFE().getListaMaterias()
    id_materias = [x[0] for x in materias]
    listaMaterias = [x[1] + " - " + x[3] + " - " + x[2] for x in materias]

    materiaSelecionada = st.selectbox("Selecione a matéria para review",
                                               listaMaterias, )

    if(materiaSelecionada == "" or materiaSelecionada == None):
        st.stop()

    st.write("Selecionou a matéria %s."%materiaSelecionada)

    i = listaMaterias.index(materiaSelecionada)
    id_materia = id_materias[i]

    texto_default = ""
    anterior_review = iFE().retornaReviewUsuario(st.session_state["user_id"], id_materia)
    if len(anterior_review) != 0:

        texto_default = anterior_review[0][3] 
        

    nota = st_star_rating("Nota:", maxValue=5, defaultValue=5)
    comentario = st.text_area("Comentário:", help="Comentário opcional que acompanhará sua nota",
                 value=texto_default)




    if(st.button("Submeter")):
        status = iFE().cadastraReview(int(st.session_state["id_user"]), int(id_materia), int(nota), comentario)
        if status == 0:
            st.write("Submeteu a review")
            st.write("Sua nota é %d"%nota)
            st.write("Seu comentário é \"%s\""%comentario)
        else:
            st.write("Houve um erro.")
        # st.session_state["nota"] = nota
        # st.session_state["comentario"] = comentario
