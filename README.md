# Python Django REST API

REST API that a basic cars makes and models database interacting with external API.

## Specifications

1) Dockerize project,
2) REST API in Django,
3) At least basic tests of endpoints and their functionality,
4) Written application must be hosted and publicly available on Heroku.

## Up and running

### Build container

> docker-compose build

### Up container

> docker-compose up

### Migrate database tables

> docker-compose run app sh -c "python manage.py migrate"

### Run tests

> docker-compose run app sh -c "python manage.py test & flake8”

## Endpoints 

### POST /cars

* Request body should contain car make and model name.
* Based on this data, its existence should be checked here https://vpic.nhtsa.dot.gov/api/.
* If the car doesn't exist - return an error.
* If the car exists - it should be saved in the database.

### POST /rate

* Add a rate for a car from 1 to 5.

### GET /cars

* Should fetch list of all cars already present in application database with their current average rate.

### GET /popular

* Should return top cars already present in the database ranking based on number of rates (not average rate values, it's important!).
