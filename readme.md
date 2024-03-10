
# Movie Recommendation System

This project is a movie recommendation system built with Streamlit, leveraging the TMDB 5000 Movies dataset. It recommends movies based on user preferences through a technique combining collaborative filtering and word vectorization. The system analyzes user ratings and movie metadata to generate personalized movie suggestions. By utilizing word vectorization, the system effectively captures the semantics of movie descriptions, enhancing the accuracy of recommendations.


## Preview
![image](https://github.com/farazabir/movie-recommender/assets/62275863/70b3416b-7c2a-4748-b0d4-9ecd06469c2a)



## Prerequisites
Python 3.8+
Docker (for containerization)

# Local Setup
Clone the repository


git clone https://github.com/farazabir/movie-recommender.git
cd movie-recommender


## Run 

### pipenv install
### pipenv shell

Navigate to the src directory and run:


 ### streamlit run app.py

The app will start running on http://localhost:8501.

# Docker Setup
 ## Build the Docker image

Navigate to the root directory of the project where the Dockerfile is located and run:

### docker build -t movie-recommender-app .
Run the container

## After building the image, run the container with:

### docker run -p 8501:8501 movie-recommender-app
Access the app by navigating to http://localhost:8501 in your web browser.
