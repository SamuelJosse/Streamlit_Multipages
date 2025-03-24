import streamlit as st

st.set_page_config(page_title='Résumé', layout="wide")

st.title("Résumé de la Session")

st.subheader("Valeur du Compteur")

if 'compteur' in st.session_state:
    st.write("Valeur actuelle :", st.session_state.compteur)    
else:
    st.write("Le compteur n'a pas encore été initalisé") 


st.subheader("Sélection d'Options")

if 'selection' in st.session_state and st.session_state.selection:
    st.write("Vous avez sélectionné les options suivantes : ")
    st.write(st.session_state.selection)
else:
    st.write("Aucune option n'a été sélectionnée")
