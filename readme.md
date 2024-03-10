
# Movie Recommendation System

This project is a movie recommendation system built with Streamlit, leveraging the TMDB 5000 Movies dataset. It recommends movies based on user preferences through a technique combining collaborative filtering and word vectorization. The system analyzes user ratings and movie metadata to generate personalized movie suggestions. By utilizing word vectorization, the system effectively captures the semantics of movie descriptions, enhancing the accuracy of recommendations.


## Preview
https://private-user-images.githubusercontent.com/62275863/311481695-70b3416b-7c2a-4748-b0d4-9ecd06469c2a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTAwNDI1MDYsIm5iZiI6MTcxMDA0MjIwNiwicGF0aCI6Ii82MjI3NTg2My8zMTE0ODE2OTUtNzBiMzQxNmItN2MyYS00NzQ4LWIwZDQtOWVjZDA2NDY5YzJhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAzMTAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMzEwVDAzNDMyNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMyOTczMWYzYzUxNDRjZjhkYWVhYjJmMDc1ZmQxNjUwYThmN2RiNTBmMGYxZjEzYTk3YTA2MjY0ZmNlNWZlOTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.qm62eGjzbB8W8Mf4Fylbt3d9jb_2oGw-d986Z1tY1Ns




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
