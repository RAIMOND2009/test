import streamlit as st

left, right = st.columns(2)

left.image("image.jpg")
right.header("Raimond Stevie")

st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.markdown("""
            - 💻Webentwicklung: Grundkenntnisse in HTML, CSS und Python
            - 💻Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            - 💻Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            - 💻Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            - 💻Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            """,unsafe_allow_html=True)

st.header("Arbeitserfahrung", anchor=False, divider="blue")

st.markdown("""
           - 🛒Berufspraktische Tage 1: Bei MAIT von 18. bis 22. Nov. 2024
           """, unsafe_allow_html=True)

st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue")

st.markdown("""
            - 🌟Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
            - 🌟Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
            - 🌟Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten
        """, unsafe_allow_html=True)

st.header("Interessen und Hobbys", anchor=False, divider="blue")

st.markdown("""
            - ⚽ Fußball: In meiner Freitzeit
            - 🏀 Basketball: In meiner Freitzeit
            - 🎮 Video Spiele: In meiner Freitzeit
         """,unsafe_allow_html=True)
