import streamlit as st
import folium


def afficher_nous_contacter():
    # Titre de la page
    st.title("Nous Joindre")


    st.subheader("Entreprise, individu, spécialiste des données")
    # Utilisation de st.write() avec du balisage HTML pour justifier le texte
    st.write("""
    <div style="text-align: justify">
    
    Avez-vous un projet de data science en tête ou simplement envie d'en savoir plus sur ce que nous pouvons accomplir ensemble ?
    Ne tardez pas à nous contacter dès aujourd'hui pour une consultation gratuite. 
    Nous sommes enthousiastes à l'idée de discuter avec vous et de concrétiser vos idées.
    
       
    </div>
    """, unsafe_allow_html=True)

    # Aller copier ce code dans formsubmit
    formulaire_de_contact = """
    <form action="https://formsubmit.co/eamoikonmichael@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder = "Votre nom" required>
         <input type="email" name="email" placeholder = "Votre email" required>
         <textarea name="message" placeholder="Ecrivez votre message ici"></textarea>
         <button type="submit">Send</button>
    </form>"""
    st.markdown(formulaire_de_contact, unsafe_allow_html=True)


    # Mise en forme avec du css
    # Utiliser le fichier css
    def fichier_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</tyle>", unsafe_allow_html=True)

    fichier_css("pages/style.css")


afficher_nous_contacter()


# Lien vers les autres pages ou sections
st.subheader("Des hyperliens vers d'autres pages ou sections")

st.write("""
- [Informations](http://localhost:8501/Information)
- [Exploration des données](http://localhost:8501/Exploration_des_donn%C3%A9es)
- [Manipulation des données](http://localhost:8501/Manipulation_des_donn%C3%A9es)
- [Modèle de prédiction](http://localhost:8501/Modele_de_prediction)
- [A Propos De Nous](http://localhost:8501/A_propos_de_nous)

""")