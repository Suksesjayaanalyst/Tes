import streamlit as st

with open("/mount/admin/install_path") as f:
    install_path = f.read().strip()

st.title("Hello Streamlit 👋")
