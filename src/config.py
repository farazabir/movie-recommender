import streamlit as st

def hide_streamlit_ui_elements():
    hide_ui_style = """
        <style>
            #MainMenu {visibility: hidden;}
            .css-12w0qpk {visibility: hidden;}
        </style>
    """
    st.markdown(hide_ui_style, unsafe_allow_html=True)
