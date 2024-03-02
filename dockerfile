FROM python:3.11-slim


WORKDIR /app


COPY . .

RUN pip install --upgrade pip && \
    pip install pipenv


RUN pipenv install --deploy --ignore-pipfile


EXPOSE 8080


ENTRYPOINT ["pipenv", "run", "streamlit", "run", "src/app.py",  "--server.port=8080", "--server.address=0.0.0.0"]
