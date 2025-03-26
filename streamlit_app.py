import streamlit as st
import home
import diabetes

st.set_page_config(page_title="Chronic Disease Prediction", layout="wide")

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Sidebar navigation buttons
with st.sidebar:
    if st.button("Home"):
        st.session_state["page"] = "Home"
    if st.button("Diabetes"):
        st.session_state["page"] = "Diabetes"

if st.session_state["page"] == "Home":
    home.show()
elif st.session_state["page"] == "Diabetes":
    diabetes.show()
