import streamlit as st
import random

if "leben" not in st.session_state:
    st.session_state.leben = 3
    st.session_state.streak = 0
    st.session_state.aufgaben = 0
    st.session_state.max_zahl = 10
    st.session_state.division = False
    st.session_state.a = 0
    st.session_state.b = 0
    st.session_state.c = 0
    st.session_state.op = "*"
    st.session_state.loesung = 0

def neue_aufgabe():
    st.session_state.op = "*" if not st.session_state.division or random.choice([True, False]) else "/"
    if st.session_state.op == "*":
        a = random.randint(1, st.session_state.max_zahl)
        b = random.randint(1, st.session_state.max_zahl)
        c = random.randint(1, st.session_state.max_zahl)
        loesung = a * b * c
    else:
        c = random.randint(1, st.session_state.max_zahl)
        b = random.randint(1, st.session_state.max_zahl)
        loesung = random.randint(1, st.session_state.max_zahl)
        a = loesung * b * c
    st.session_state.a = a
    st.session_state.b = b
    st.session_state.c = c
    st.session_state.loesung = loesung

if st.session_state.a == 0:
    neue_aufgabe()

st.title("Interaktiver Mathe-Rechner")

st.write(f"Leben: {'❤️' * st.session_state.leben}")
st.write(f"Aktuelle Serie: {st.session_state.streak}")
st.write(f"Gelöste Aufgaben: {st.session_state.aufgaben}")

if st.session_state.leben > 0:
    st.write(f"{st.session_state.a} {st.session_state.op} {st.session_state.b} {st.session_state.op} {st.session_state.c}")
    antwort = st.number_input("Deine Antwort", step=1)

    if st.button("Bestätigen"):
        if antwort == st.session_state.loesung:
            st.session_state.streak += 1
            st.session_state.aufgaben += 1
            if st.session_state.streak == 10:
                st.session_state.division = True
            if st.session_state.streak == 15:
                st.session_state.max_zahl = 20
        else:
            st.session_state.leben -= 1
            st.session_state.streak = 0
        neue_aufgabe()
        st.rerun()
else:
    st.subheader("Spiel vorbei")
    if st.button("Neustarten"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
