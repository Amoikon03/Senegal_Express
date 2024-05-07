# Importation des librairies
import streamlit as st
import pandas as pd


# Personnalisation de l'affichag
st.title("Exploration des données")


# Charger le fichier csv
df = pd.read_csv("Expresso.csv")


# Afficher la forme du DataFrame (nombre de lignes et de colonnes)
st.write("### Forme du DataFrame : ")
lign, col = df.shape
st.write(f"Le nombre de lignes dans le DataFrame est : {lign}")
st.write(f"Le nombre de colonnes dans le DataFrame est : {col}")


# Afficher les premières lignes du DataFrame
st.write("### Premières lignes du DataFrame : ")
st.write(df.head())


# Afficher les informations sur les colonnes (type de données, valeurs manquantes, etc.)
st.write("### Informations sur les colonnes : ")
st.write(df.info())

# Vérification des valeurs manquantes
valeurs_manquantes = df.isnull().sum()
valeurs_manquantes  = pd.DataFrame(valeurs_manquantes).T
st.write("### **Valeurs manquantes par colonne :** \n", valeurs_manquantes)

# Vérification des valeurs aberrantes
st.write("### **Les valeurs aberrantes :**")
# Définir le seuil pour identifier les valeurs aberrantes en fonction du score Z
seuil_z = 3


# Boucle à travers chaque colonne
for colonne in df.select_dtypes(include=['int64', 'float64']).columns:
    # Calculer la moyenne et l'écart-type de la colonne actuelle
    moyenne = df[colonne].mean()
    ecart_type = df[colonne].std()

    # Calculer les scores Z pour la colonne actuelle
    scores_z = (df[colonne] - moyenne) / ecart_type

    # Identifier les valeurs aberrantes pour la colonne actuelle
    valeurs_aberrantes = df[abs(scores_z) > seuil_z]

    # Afficher les valeurs aberrantes pour la colonne actuelle
    if not valeurs_aberrantes.empty:
        st.write(f"Valeurs aberrantes dans la colonne '{colonne}':")
        for index, valeur in valeurs_aberrantes[colonne].items():
            st.write(f"Ligne: {index}, Valeur: {valeur}")

# Autre methode pour calculer le z-score
#for colonne in df.select_dtypes(include=["int64", "float64"]).columns :
    #z_score = (df[colonne] - df[colonne].mean()) / df[colonne].std()


# Afficher les statistiques descriptives pour les colonnes numériques
st.write("### **Statistiques descriptives pour les colonnes numériques :**")
st.write(df.describe())


# Titre de l'application
#st.write("### **Pandas Profiling**")

# Lien vers les autres pages ou sections
st.subheader("Des hyperliens vers d'autres pages ou sections")

st.write("""
- [Informations](http://localhost:8501/Information)
- [Manipulation des données](http://localhost:8501/Manipulation_des_donn%C3%A9es)
- [Modèle de prédiction](http://localhost:8501/Modele_de_prediction)
- [Nous Contacter](http://localhost:8501/A_propos_de_nous)
- [A Propos De Nous](http://localhost:8501/A_propos_de_nous)

""")