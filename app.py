import streamlit as st
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- HEADER SECTION ----#
with st.container():
    st.subheader("Hey, I am Denis :wave:")
    st.title("A Data Engineer from Bulgaria")
    st.write("This is a test page. You can find some of my projects on Github:")
    st.write("(https://github.com/DenislavDyakov)")

# ---- LOAD ASSETS ----#
lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_rdjfuniz.json")


# ---- HEADER SECTION ----#
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            working with:
            - SQL
            - Python
            - Tableau
            - and others
            """
        )
    with right_column:
        st_lottie(lottie_animation, )
