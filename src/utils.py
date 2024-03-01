import requests

def get_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a473717550744f04f45b29b1046372d9')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

def recommend_movies(movie, movies, similarity):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = [] 
    recommend_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id 
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(get_poster(movie_id))

    return recommend_movies, recommend_movies_poster
