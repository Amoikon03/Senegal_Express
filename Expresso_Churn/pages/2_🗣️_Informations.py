# Importater les librairies
import streamlit as st
import pandas as pd

# Titre de la page
st.title("**Les informations relatives à ces données.**")


# Instruction
# Utilisation de HTML pour styliser le texte avec un fond jaune
# st.markdown('<div style="background-color: green; padding: 10px;">Voici les données pour réaliser cette application</div>', unsafe_allow_html=True)


# Chargement de données du fichier csv
df = pd.read_csv("Expresso.csv")


# Afficher les noms des données
st.warning("Les données nécessaires pour élaborer cette application sont les suivantes.")
st.write(df)

# Afficher les noms des colonnes
st.subheader("**Des informations concernant les noms des colonnes.**")

st.write("**user_id**")
st.write("**REGION** : la localité de chaque client")
st.write("**TENURE** : la durée dans le reseau")
st.write("**MONTANT** : montant de recharge")
st.write("**FREQUENCE_RECH** : nombre de fois que le client a fait une recharge")
st.write("**REVENUE** : revenu mensuel de chaque client")
st.write("**ARPU_SEGMENT** : revenu sur 90 jours/3")
st.write("**FREQUENCE** : nombre de fois que client à fait un revenu")
st.write("**DATA_VOLUME** : nombre de connexions")
st.write("**ON_NET** : appel inter expresso")
st.write("**ORANGE** : appel vers orange")
st.write("**TIGO** : appel vers Tigo")
st.write("**ZONE1** : appel vers les zone1")
st.write("**ZONE2** : appel vers les zone2")
st.write("**MRG** : un client qui fait du vas")
st.write("**REGULARITY** : nombre de fois que le client est actif pendant 90 jours")
st.write("**TOP_PACK** :les pack les plus activés")
st.write("**FREQ_TOP_PACK** : nombre de fois que le client a activé les packages top pack")
st.write("**CHURN** : variable à predire-Target")


# Lien vers les autres pages ou sections
st.subheader("Des hyperliens  vers d'autres pages ou sections")


# Liste des liens
st.write("""
- [Exploration des données](http://localhost:8501/Exploration_des_donn%C3%A9es)
- [Manipulation des données](http://localhost:8501/Manipulation_des_donn%C3%A9es)
- [Modèle de prédiction](http://localhost:8501/Modele_de_prediction)
- [Nous Contacter](http://localhost:8501/A_propos_de_nous)
- [A Propos De Nous](http://localhost:8501/A_propos_de_nous)

""")