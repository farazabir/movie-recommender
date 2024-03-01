import os
import pandas as pd
import pickle

def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    movie_dict_path = os.path.join(base_dir, 'data', 'movies_dict.pkl')
    similarity_path = os.path.join(base_dir, 'data', 'similarity.pkl')
    
    with open(movie_dict_path, 'rb') as file:
        movie_dict = pickle.load(file)
    movies = pd.DataFrame(movie_dict)
    
    with open(similarity_path, 'rb') as file:
        similarity = pickle.load(file)
    
    return movies, similarity
