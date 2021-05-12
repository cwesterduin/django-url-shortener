# LAP 4 Code Challenge

## Installation and Usage

### Installation
- clone or download the repo
- navigate to the root folder
- run `pipenv shell` to enter a virtual env
- run `pipenv install` to install dependencies

### Usage
- first start the database
    - run `docker-compose up`
        - to enter db run `docker exec -it django-url-shortener_db_1 mongo -u user -p password`
    - to stop run `docker-compose down --remove-orphans --volumes`
- to start the server run `python manage.py runserver`

### Wins 
- we successfully made a URL shortener using Python Django 
- made used a MongoDB database which we had to configure in a different way to postgreSQL and learnt how to do this in the process
- our page renders as it is supposed to with a working form 
- the routes to admin is also functioning as intended

### Challenges 
- The main challenge was using MongoDB instead of SQL for this project
- we initially weren't sure how to configure this for Django but we used a Djongo documentation to work this out
- we also had to configure the docker-compose file so that our app rendered on the localhost port as desired 
- the app main used Djongo and Django installations 
- we also had issues getting the id from the db which we had wanted to do as our models was not responding with Django Admin initially

Enjoy our App :) 