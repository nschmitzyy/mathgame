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
    st.session_state.eingabe = ""

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

st.title("🧮 Mathe-Rechner")

st.write(f"Leben: {'❤️' * st.session_state.leben}")
st.write(f"Serie: {st.session_state.streak}")
st.write(f"Aufgaben: {st.session_state.aufgaben}")

if st.session_state.leben > 0:
    st.markdown(
        f"<div style='font-size:32px;text-align:center;padding:10px;border:2px solid #444;border-radius:10px;'>{st.session_state.a} {st.session_state.op} {st.session_state.b} {st.session_state.op} {st.session_state.c}</div>",
        unsafe_allow_html=True
    )

    def check_answer():
        if st.session_state.eingabe != "":
            try:
                if int(st.session_state.eingabe) == st.session_state.loesung:
                    st.session_state.streak += 1
                    st.session_state.aufgaben += 1
                    st.session_state.eingabe = ""
                    if st.session_state.streak == 10:
                        st.session_state.division = True
                    if st.session_state.streak == 15:
                        st.session_state.max_zahl = 20
                else:
                    st.session_state.leben -= 1
                    st.session_state.streak = 0
                    st.session_state.eingabe = ""
                neue_aufgabe()
            except ValueError:
                st.session_state.eingabe = ""

    # Eingabefeld mit Autofocus
    st.text_input(
        "Deine Antwort",
        key="eingabe",
        on_change=check_answer,
        label_visibility="collapsed",
        placeholder="Gib hier deine Antwort ein",
        autofocus=True
    )

    cols = st.columns(3)
    for i, num in enumerate(range(1, 10)):
        if cols[i % 3].button(str(num)):
            st.session_state.eingabe += str(num)
            st.rerun()

    col1, col2, col3 = st.columns(3)
    if col1.button("0"):
        st.session_state.eingabe += "0"
        st.rerun()
    if col2.button("⌫"):
        st.session_state.eingabe = st.session_state.eingabe[:-1]
        st.rerun()
    if col3.button("C"):
        st.session_state.eingabe = ""
        st.rerun()

else:
    st.subheader("Spiel vorbei")
    if st.button("Neustarten"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
