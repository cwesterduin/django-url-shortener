# LAP 4 Code Challenge

## Installation and Usage

# Installation
- clone or download the repo
- navigate to the root folder
- run `pipenv shell` to enter a virtual env
- run `pipenv install` to install dependencies

# Usage
- first start the database
    - run `docker-compose up`
        - to enter db run `docker exec -it django-url-shortener_db_1 mongo -u user -p password`
    - to stop run `docker-compose down --remove-orphans --volumes`
- to start the server run `python manage.py runserver`

