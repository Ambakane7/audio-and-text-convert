import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

# Titre de l'application
st.markdown("<h3 style ='text-align:center;'>AW BISSIMILA TEXT AND AUDIO CONVERTER  KAN</h3>", unsafe_allow_html=True)
st.markdown("<h4 style ='text-align:center;color: green'>Auteur : Mr_G</h4>", unsafe_allow_html=True)


# Sous-titre pour la conversion texte vers audio
st.subheader("Texte vers audio")

# Zone de saisie pour entrer le texte
text = st.text_input("Entrez le texte que vous souhaitez convertir en audio et tapez sur ta touche ENTRE")
 ##################################################################
 
 # URL input
url = st.text_input(" ou Entrez l'URL de l'article:", "https://onef.ml/mot-du-directeur-general/")

# Language selection
language = st.selectbox("Choisir une langue:", options=["fr", "en"])

# Convert button
if st.button("Convertir en audio"):
    st.write("Téléchargement de l'article...")
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    st.write("Conversion du texte en audio...")
    my_audio = gTTS(text=article.text, lang=language, slow=False)
    my_audio.save('presentation.mp3')

    st.write("Lecture de l'audio...")
    audio_file = open('presentation.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
#####################################################################################

# Vérification de la saisie utilisateur
if text:
    # Choix de la langue pour la synthèse vocale
    lang = st.selectbox("Choisissez la langue", ["fr", "en"])

    # Création du fichier audio avec gTTS
    tts = gTTS(text=text, lang=lang)
    filename = "audio.mp3"
    tts.save(filename)

    # Lecture du fichier audio avec Streamlit
    audio_file = open(filename, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# Sous-titre pour la conversion audio vers texte
st.subheader("Audio vers texte")

# Zone de saisie pour uploader le fichier audio
audio_file = st.file_uploader("Chargez votre fichier audio", type=["mp3", "wav"])

# Vérification de la saisie utilisateur
if audio_file:
    # Lecture du fichier audio avec SpeechRecognition
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="fr-FR")

    # Affichage du texte reconnu
    st.write("Le texte reconnu est:")
    st.write(text)
