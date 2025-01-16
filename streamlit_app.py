import streamlit as st
from pathlib import Path


st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)


def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'Lebenslauf1.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns(2)

left.image("rr.png", width=250)

with right:
    right.markdown("""
               <h3>Raimond Stevie</h3>
               <br>
               <em>Ich bin davon überzeugt, dass IT die Welt ändern wird
               und ich möchte ein teil davon sein.</em>
               """, unsafe_allow_html=True)


    st.download_button(
        label="📄 Download Lebenslauf",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )
    st.write("📩", "raimond.stevie@gmx.at")
        

st.header("IT-Kompetenzen", anchor=False, divider="blue")

st.markdown("""
            - 💻Webentwicklung: Grundkenntnisse in HTML, CSS und Python.
            - 💻Programmierung: Websiten erstellen, basic tools kennen.
            - 💻Office-Apps: guter Umgang mit Microsoft Word, Excel und PowerPoint.
            - 💻Eigene Projekte: Eigene Websiten erstellen, programiersprachen ausprobieren.
            - 💻Schulprojekte: Präsentationen erstellen, Streamlit benützen.
            """,unsafe_allow_html=True)

st.header("Arbeitserfahrung", anchor=False, divider="blue")

st.markdown("""
           - 🛒Berufspraktische Tage 1: Bei MAIT von 18. bis 22. Nov. 2024
           """, unsafe_allow_html=True)

st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue")

st.markdown("""
            - 🌟Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien.
            - 🌟Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich.
            - 🌟Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten.
        """, unsafe_allow_html=True)

st.header("Interessen und Hobbys", anchor=False, divider="blue")

st.markdown("""
            - ⚽ Fußball: In meiner Freitzeit.
            - 🏀 Basketball: In meiner Freitzeit.
            - 🎮 Video Spiele: In meiner Freitzeit.
         """,unsafe_allow_html=True)
