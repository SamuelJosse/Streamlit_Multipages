import streamlit as st
import plotly.express as px

st.title("Visualisation des données")

if 'df' in st.session_state:
    df = st.session_state['df']
    
    
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns
    
    if len(numeric_columns) >= 2:
        x_axis = st.selectbox(
            "Séléctionnez la colonne pour l'axe X",
            options=numeric_columns
        )
        
        y_axis = st.selectbox(
            "Séléctionnez la colonne pour l'axe Y",
            options=numeric_columns
        )
        
        fig = px.scatter(st.session_state.df, x=x_axis, y=y_axis)
        
        st.plotly_chart(fig)
    else:
        st.warning('Le fichier CSV doit contenir au moins deux colonnes numériques')
    
else:
    st.error("Aucun DataFrame trouvé. Veuillez charger un fichier CSV de puis la page d'Accueil")

    


    
    
    
    

