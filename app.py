import streamlit as st
from utils import recommend_movies
from config import hide_streamlit_ui_elements
from data_loader import load_data

movies, similarity = load_data()

hide_streamlit_ui_elements()

# UI to select a movie
selected_movie = st.selectbox('Select Movie Name', movies['title'].values)

def view():
    names, posters = recommend_movies(selected_movie, movies, similarity)
     
    columns_per_row = 3

    rows = len(names) // columns_per_row + (1 if len(names) % columns_per_row else 0)
    
    index = 0
    for _ in range(rows):
        cols = st.columns(columns_per_row)
        for col in cols:
            if index < len(names):
                with col:
                    st.markdown(f"<div style='font-size: 16px;'>{names[index]}</div>", unsafe_allow_html=True)
                    st.image(posters[index], use_column_width=True)
                index += 1

view()
