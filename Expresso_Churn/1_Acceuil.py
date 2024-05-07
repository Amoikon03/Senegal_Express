# Importer les librairies
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title= "Application Expresso",
    page_icon= "☏"

)

# Titre de page
st.title("Prédiction de Churn chez Expresso")

# Image illustrative de l'application
img = Image.open("expresso.jpg")

# Titre et description de l'application
st.image(img, width=50, caption="Image d'expresso sur google", use_column_width=True)
# Utilisation de st.write() avec du balisage HTML pour justifier le texte
st.write("""
<div style="text-align: justify">
    Bienvenue dans l'application de prédiction de churn d'Expresso. Cette application vous permet de prédire 
    le churn (désabonnement) des clients en fonction de leurs caractéristiques. Entrez les valeurs des 
    caractéristiques dans le panneau latéral pour obtenir une prédiction.
</div>
""", unsafe_allow_html=True)

# Fonctionnalier de l'application
st.header("Fonctionnalités de l'application")

# A propos de l'application
st.write("""
<div style="text-align: justify">
 Bienvenue dans l'application de prédiction de désabonnement d'Expresso. Cette application vous permet de prédire
 le désabonnement des clients en fonction de leurs caractéristiques.
</div>
""", unsafe_allow_html=True)

st.write(" ")

# Information sur les donnnées
st.write("**Informations sur les données :** Information sur les donnnées")


# Exploration des données
st.write("**Exploration des données :** Exploration des données")


# Data manipulation
st.write("**Manipulation des données :** Manipulations des données")


# Data modélisation
st.write("**Modélisation :** Création des modèles de machine learning et de deep learning")


# Prendre contact
st.write("**Contactez Nous :** Prendre contact pour plus d'information")


# A propos de nous
st.write("**A Propos De Nous :** Qui sommes nous et comment nous rejoindre")


# Lien vers les autres pages ou sections
st.subheader("Des hyperliens vers d'autres pages ou sections")


st.write("""
- [Informations](http://localhost:8501/Information)
- [Exploration des données](http://localhost:8501/Exploration_des_donn%C3%A9es)
- [Manipulation des données](http://localhost:8501/Manipulation_des_donn%C3%A9es)
- [Modèle de prédiction](http://localhost:8501/Modele_de_prediction)
- [Nous Contacter](http://localhost:8501/A_propos_de_nous)
- [A Propos De Nous](http://localhost:8501/A_propos_de_nous)

""")