import streamlit as st
import random

# Liste des pays du monde
with open("countries.txt") as f:
    COUNTRIES = [line.strip() for line in f.readlines()]

def app():
    # Initialisation des états
    if "selected_countries" not in st.session_state:
        st.session_state.selected_countries = []

    if "current_country" not in st.session_state:
        st.session_state.current_country = ""

    # Affichage de l'application
    st.title("Roue des Pays")

    # Bouton pour lancer la roue
    if st.button("Lancer la roue"):
        st.session_state.current_country = random.choice(COUNTRIES)
        if st.session_state.current_country not in st.session_state.selected_countries:
            st.session_state.selected_countries.append(st.session_state.current_country)

    # Affichage du pays sélectionné
    if st.session_state.current_country:
        st.markdown(f"### **{st.session_state.current_country}**")

    # Affichage des pays déjà sélectionnés
    if st.session_state.selected_countries:
        st.markdown("#### Pays déjà sélectionnés :")
        st.write(", ".join(st.session_state.selected_countries))

    # Bouton pour réinitialiser
    if st.button("Réinitialiser"):
        st.session_state.selected_countries = []
        st.session_state.current_country = ""

if __name__ == "__main__":
    app()
