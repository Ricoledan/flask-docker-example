# flask-docker-example

🐍 example code for a containerized Flask Application using Docker

## setup

install dependencies
`pip install -r requirements.txt`

run application
`python main.py`

## docker commands

build image
`docker build -t dockerized_flask:latest .`

start container
`docker run --name dockerized_flask_container -p 5000:5000 -d dockerized_flask:latest`
