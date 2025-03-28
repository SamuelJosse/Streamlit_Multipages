import streamlit as st


st.set_page_config(page_title='Sélecteur', layout="wide")

st.title("Page de sélection")

if 'selection' not in st.session_state:
    st.session_state.selection = []
    
selection_placeholder = st.empty()

st.subheader("Ajouter une option")

option = st.selectbox(
    "Choisissez une option à ajouter",
    ["Option A", "Option B", "Option C", "Option D"],
    key='add_selectbox',
)


if st.button("Ajouter à la sélection", key="add_buton"):
    if option not in st.session_state.selection:
        st.session_state.selection.append(option)
        st.success(f'Option "{option}" ajoutée à la sélection.')
    else:
        st.warning(f'Option "{option}" est déjà dans la sélection.')
        
        
st.subheader("Supprimer une option")

if st.session_state.selection:
    
    remove_option = st.selectbox(
        "Choisissez une option à supprimer",
        st.session_state.selection,
        key='remove_selectbox'
    )
    
    if st.button("Supprimer une option"):
        st.session_state.selection.remove(remove_option)
        st.success(f'Option "{remove_option}" supprimée de la sélection.')
else:
    st.info("Aucune option à supprimer")



if st.session_state.selection:
    selection_placeholder.write(st.session_state.selection)
else:
    selection_placeholder.write('### Sélection actuelle : Aucune option sélectionnée')


        

