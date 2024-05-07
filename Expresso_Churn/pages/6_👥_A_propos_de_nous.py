import streamlit as st
import streamlit as st
import pickle as pk


def afficher_about_us():
    # Titre de la page

    st.title('A prospos de nous')

    def apropos():
        # Définition du style CSS pour justifier le texte
        st.markdown("""
            <style>
            /* Définition du style pour justifier le texte */
            .css-1aumxhk {
                text-align: justify;
            }
            </style>
            """, unsafe_allow_html=True)

        st.write("Bienvenue sur **CHURN-EXPRESSO** !")
        st.write("""
        <div style="text-align: justify">
         Nous sommes une équipe passionnée par la data science et par son potentiel illimité pour convertir les données en insights puissants. 
        Notre équipe se compose de [nombre] professionnels expérimentés de la data science, chacun apportant sa propre expertise et sa passion unique à chaque projet.
        </div>
        """, unsafe_allow_html=True)

        st.header("Notre Vision")
        # Utilisation de st.write() avec du balisage HTML pour justifier le texte
        st.write("""
        <div style="text-align: justify">
        Nous aspirons à créer un avenir où les données jouent un rôle central dans l'innovation et la prise de décision dans tous les domaines. 
        Nous sommes convaincus que la data science a le pouvoir de résoudre certains des défis les plus urgents de notre époque, qu'il s'agisse 
        de problèmes complexes en entreprise, de questions sociales ou d'enjeux environnementaux.
        Notre vision est de voir un monde où chaque décision est éclairée par des données fiables et des analyses approfondies, permettant ainsi 
        aux entreprises et aux organisations de prospérer dans un monde en constante évolution.
        </div>
        """, unsafe_allow_html=True)

        st.header("Notre Mission")
        # Utilisation de st.write() avec du balisage HTML pour justifier le texte
        st.write("""
        <div style="text-align: justify">
        Nous avons pour objectif de rendre l'analyse de données avancée accessible à tous et de rendre les insights compréhensibles et utilisables pour chacun. 
        Nous sommes convaincus que la data science devrait être à la portée de tous, indépendamment de leur niveau de compétence technique.
        C'est pourquoi nous nous efforçons de développer des outils intuitifs et conviviaux qui permettent de transformer les données brutes en informations exploitables.
        </div>
        """, unsafe_allow_html=True)

        st.header("Notre Passion")
        # Utilisation de st.write() avec du balisage HTML pour justifier le texte
        st.write("""
        <div style="text-align: justify">
        Notre moteur, c'est notre passion pour les données. Nous sommes passionnés par l'exploration de nouveaux ensembles de données, la révélation de tendances cachées et la narration de récits captivants à travers les données. 
        Chaque projet représente pour nous une nouvelle aventure, et nous sommes toujours enthousiastes à l'idée d'explorer les innombrables possibilités qu'offrent les données.
        </div>
        """, unsafe_allow_html=True)

        st.header("Pourquoi Nous Choisir")

        # Utilisation de st.write() avec du balisage HTML pour justifier le texte
        st.write("""
        <div style="text-align: justify">
        Lorsque vous choisissez de travailler avec notre équipe, vous accédez à une expertise de haut niveau, portée par des professionnels passionnés et dévoués. 
        Nous sommes prêts à relever les défis les plus exigeants en matière de data science.
        Notre engagement se traduit par la fourniture de solutions sur mesure et novatrices, parfaitement adaptées à vos besoins et objectifs commerciaux.
        Que vous dirigiez une jeune start-up ou une entreprise établie, notre mission est de vous aider à exploiter pleinement le potentiel de vos données
        et à prendre des décisions stratégiques éclairées pour l'avenir de votre entreprise.
        </div>
        """, unsafe_allow_html=True)



        st.write("[Nous contacter](http://localhost:8501/A_propos_de_nous)")
        st.write("**Adresse e-mail :** eamoikonmichael@gmail.com")
        st.markdown("**Téléphone :** [+225 07 07 74 62 59](tel:+225 0707746259)")
        st.write("**Localisation :** [Bouaké, Gonfreville]")

    apropos()

afficher_about_us()

# Lien vers les autres pages ou sections
st.subheader("Des hyperliens vers d'autres pages ou sections")


st.write("""
- [Informations](http://localhost:8501/Information)
- [Exploration des données](http://localhost:8501/Exploration_des_donn%C3%A9es)
- [Manipulation des données](http://localhost:8501/Manipulation_des_donn%C3%A9es)
- [Modèle de prédiction](http://localhost:8501/Modele_de_prediction)

""")



