import streamlit as st

st.set_page_config(page_title='Compteur', layout="wide")

st.title("Page du compteur")



if 'compteur' not in st.session_state:
    st.session_state.compteur = 0
    
increment = st.number_input("Valeur à ajouter", min_value=1, value=1)

if st.button("Incrémenter"):
    st.session_state.compteur += increment
    
st.write("Valeur actuelle :", st.session_state.compteur)

st.divider()

compteur_sans_session = 0

if st.button("Incrémenter (sans session)"):
    compteur_sans_session += 1

st.write("Valeur du compteur (sans session) :", compteur_sans_session)

 




