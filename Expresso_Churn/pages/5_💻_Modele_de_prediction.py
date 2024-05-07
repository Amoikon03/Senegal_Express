# Import des bibliothèques
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Fonction pour charger les données à partir du fichier pickle
@st.cache_data
def load_data(filename):
    return pd.read_pickle(filename)

# Fonction pour prédire churn
def predict_churn(input_data, model):
    return model.predict(input_data)

# Fonction principale pour l'interface utilisateur Streamlit
def main():
    # Titre de la page
    st.title("Modèle de Prédiction")

    # Chargement des données à partir du fichier pickle
    df = load_data(r"C:\EAM\Expresso\data_frame.pkl")

    # Entraînement du modèle d'apprentissage automatique avec Random Forest
    st.header("Entraînement du modèle d'apprentissage automatique (Random Forest)")

    # Diviser les données en ensemble d'entraînement et ensemble de test
    X = df.drop(columns=['CHURN'])
    y = df['CHURN']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner un modèle de classification Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Faire des prédictions sur l'ensemble de test avec Random Forest
    y_pred_rf = rf_model.predict(X_test)

    # Évaluer les performances du modèle Random Forest
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    precision_rf = precision_score(y_test, y_pred_rf, average='weighted')
    recall_rf = recall_score(y_test, y_pred_rf, average='weighted')
    f1_rf = f1_score(y_test, y_pred_rf, average='weighted')
    auc_rf = roc_auc_score(y_test, y_pred_rf, multi_class='ovo')

    # Afficher les métriques de performance de Random Forest
    st.subheader("Métriques de performance (Random Forest)")
    st.write("Accuracy :", accuracy_rf)
    st.write("Précision :", precision_rf)
    st.write("Rappel :", recall_rf)
    st.write("F-score :", f1_rf)
    st.write("AUC :", auc_rf)

    # Entraînement du modèle d'apprentissage automatique avec Régression Logistique
    st.header("Entraînement du modèle d'apprentissage automatique (Régression Logistique)")

    # Entraîner un modèle de régression logistique
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)

    # Faire des prédictions sur l'ensemble de test avec Régression Logistique
    y_pred_lr = lr_model.predict(X_test)

    # Évaluer les performances du modèle Régression Logistique
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    precision_lr = precision_score(y_test, y_pred_lr, average='weighted')
    recall_lr = recall_score(y_test, y_pred_lr, average='weighted')
    f1_lr = f1_score(y_test, y_pred_lr, average='weighted')
    auc_lr = roc_auc_score(y_test, y_pred_lr, multi_class='ovo')

    # Afficher les métriques de performance de Régression Logistique
    st.subheader("Métriques de performance (Régression Logistique)")
    st.write("Accuracy :", accuracy_lr)
    st.write("Précision :", precision_lr)
    st.write("Rappel :", recall_lr)
    st.write("F-score :", f1_lr)
    st.write("AUC :", auc_lr)

    # Interface utilisateur pour les prédictions
    st.header("Interface utilisateur pour les prédictions")

    # Ajouter des champs d'entrée pour les caractéristiques et un bouton de validation
    st.sidebar.subheader("Entrer les valeurs des caractéristiques")

    # Saisie des valeurs des caractéristiques
    feature_1_value = st.sidebar.number_input("Durée d'appel (en minutes)", value=100.0)
    feature_2_value = st.sidebar.selectbox("Type de contrat", ["Forfait mensuel", "Forfait annuel", "Carte prépayée"],
                                           index=0)
    feature_3_value = st.sidebar.number_input("Nombre de SMS envoyés", value=50)
    feature_4_value = st.sidebar.number_input("Âge du client", value=30)
    feature_5_value = st.sidebar.number_input("Revenu mensuel (en fcfa)", value=500)
    feature_6_value = st.sidebar.selectbox("Type de connexion", ["3G", "4G", "5G"], index=0)
    feature_7_value = st.sidebar.checkbox("Forfait Internet illimité")

    # Bouton de sélection de modèle
    model_choice = st.sidebar.radio("Choisir le modèle", ("Random Forest", "Régression Logistique"))

    # Bouton de validation pour faire des prédictions
    if st.sidebar.button("Prédire"):
        # Création d'un DataFrame avec les valeurs saisies par l'utilisateur
        input_data = pd.DataFrame({
            'user_id': [12345],  # Valeur pour user_id
            'REGION': [0],# Remplacez par la valeur appropriée
            'TENURE': [10],  # Remplacez par la valeur appropriée
            'MONTANT': [100],  # Remplacez par la valeur appropriée
            'FREQUENCE_RECH': [5],  # Exemple de valeur pour une caractéristique manquante
            'REVENUE': [20000],  # Exemple de valeur pour une caractéristique manquante
            'ARPU_SEGMENT': [10000],  # Exemple de valeur pour une caractéristique manquante
            'FREQUENCE': [10],  # Exemple de valeur pour une caractéristique manquante
            'DATA_VOLUME': [5000],  # Exemple de valeur pour une caractéristique manquante
            'ON_NET': [100],  # Exemple de valeur pour une caractéristique manquante
            'ORANGE': [50],  # Exemple de valeur pour une caractéristique manquante
            'TIGO': [20],  # Exemple de valeur pour une caractéristique manquante
            'ZONE1': [10],  # Exemple de valeur pour une caractéristique manquante
            'ZONE2': [5],  # Exemple de valeur pour une caractéristique manquante
            'MRG': [0],  # Valeur pour MRG
            'REGULARITY': [12],  # Exemple de valeur pour une caractéristique manquante
            'TOP_PACK': [20],  # Exemple de valeur pour une caractéristique manquante
            'FREQ_TOP_PACK': [3],  # Exemple de valeur pour une caractéristique manquante
        })

        # Faire une prédiction avec les deux modèles entraînés
        prediction_rf = predict_churn(input_data, rf_model)
        prediction_lr = predict_churn(input_data, lr_model)

        # Affichage des prédictions
        st.write("Prédiction de churn (Random Forest) :", prediction_rf)
        st.write("Prédiction de churn (Régression Logistique) :", prediction_lr)


# Exécution de l'application principale
if __name__ == "__main__":
    main()

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