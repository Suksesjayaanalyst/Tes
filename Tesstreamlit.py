import streamlit as st

try:
    with open("/mount/admin/install_path") as f:
        install_path = f.read().strip()
except FileNotFoundError:
    install_path = "Not found (default or dev environment)"

st.title("Hello Streamlit 👋")
st.write(f"Install Path: {install_path}")
