# Sprocket Factory Challenge

## Description
A simple REST API that allows reading and writing of data for a hypothetical small sprocket factory.

It has three entities: Sprockets, Factories, and Production.

Sprockets have descriptions of all the different types of sprockets. Factories have names. Production has a factory ID and records of the sprockets produced in that factory, the sprocket production goal, and the date of production.

![imagen.png](data:image/png;base64,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)

## Endpoints

A limited number of endpoints are available. They are as follows:

`GET /sprocketFactory/v1/production`

Returns a list of all the production records for all the factories.

`GET /sprocketFactory/v1/production/{id}`

Returns a list of all the production records for the specified factory id.

`GET /sprocketFactory/v1/sprockets`

Returns a list of all the sprockets in the database.

`GET /sprocketFactory/v1/sprockets/{id}`

Returns the sprocket with the specified id.

`POST /sprocketFactory/v1/sprockets`

Creates a new sprocket.

`PUT /sprocketFactory/v1/sprockets/{id}`

Updates the sprocket with the specified id.

## Requirements
- python 3.10
- pip

Optional:
- virtualenv
- docker for DB

## Installation
1. Clone the repository
1. (Optional) Create and activate a virtual environment
    ```
    python -m venv .venv
    In Linux: source .venv/bin/activate 
    In Windows: .venv\Scripts\activate.bat
    ```
1. Install the requirements
    ```
    pip install -r requirements.txt
    ```
1. (Optional) Start the database. Is a docker container with postgresql
    ```
    docker-compose up -d
    ```
1. (Optional) Populate the database with some testing data
    ```
    python populate_db.py
    ```
1. Configure the .env file to change the database connection parameters. By default it uses the docker container, but change it to your needs.
    ```
    cp .env.example .env
    ```
1. Finally, start the application
    ```
    python run.py
    ```

## Testing
The application has a few tests. To run them, simply execute the following command:
```
python -m pytest
```

To run the tests with coverage, execute the following command:
```
python -m pytest --cov
```



## FAQ
### Why Flask?
I selected Flask as the framework for this project because of its lightweight and flexible nature, which makes it easy to use and deploy. Furthermore, its easy-to-use debugging tools are a major advantage. Unlike some other frameworks, Flask does not have an integrated ORM, which I view as a positive feature, as it allows you to choose the ORM that best fits your needs. In my case, I chose to use SQLAlchemy. Although it is possible to develop a project without an ORM, this is generally not advisable for real projects.

Flask's decorator-based routing system and easy json response is another aspect that I appreciate, as it is simple to use and allows for the creation of fully flexible REST APIs.

Although Django is a powerful framework, I felt it was overkill for this small project due to its heavy and complex nature. Additionally, its opinionated structure, which is usually a good thing, did not fit the needs of this particular project. While it does have a built-in ORM, it lacks flexibility and is not well-suited for quick deployment on a project of this size. Although Django Rest Framework is a powerful tool for creating REST APIs using django-rest-framework, it is also opinionated and requires more configuration than creating a REST API from scratch in Flask, which is better suited for tiny and quick projects like this.

I know there are other frameworks, such as FastAPI, but in this case I decided to go with Flask because it is a framework that I am more familiar.

### Why three different tables?

Although it was not strictly necessary to have three separate tables, I chose to do so in order to follow good database normalization practices. This approach makes the database more flexible and easier to understand, and it optimizes record and index addition. Upon reviewing the data in the provided JSON file, particularly the production records, I noticed that the timestamps were in integer form and that each factory had three columns. Based on this information, I decided to create three columns in the production table and include a foreign key to the factory table.

While the factory table is not strictly required and its "name" column is not on the original data, I opted to create them anyway. This decision further normalizes the data, making it easier to add new factories, production records, or indexes.

### Is pylint necessary?

Well, it's not strictly necessary, of course, but I like to use it to keep my code clean and consistent, specially when working in a team. As any python programmer knows, _readability counts_ and it's almost mandatory to follow the PEP8 guidelines. However, pylint can be quite strict, and it may be necessary to disable some rules when working with certain frameworks, such as Flask. Although I worked on this project alone and it was a quick project, when working as part of a team, it is important to establish which rules are essential and which can be ignored.

### Where are the microservices?

Considering the limited size and time constraints of this project, I decided that creating a single program was sufficient. However, if this project were to expand in scope, I would recommend creating a microservice for each entity, such as sprocket, factory, and production, as well as one for the endpoint, or maybe another architecture. Using microservices would improve scalability and facilitate maintenance.

Creating such a system would require many things, such as a broker system, a deployer, and  maybe a framework specifically for microsystems. Nevertheless, given the scope of this project, I decided to keep it simple and create a single program.

### Git commits

In this proyect, with no mandatory commit policy, no issue tracker, no backlog, etc... I decided to commit as I go, and to keep the commits as small as possible but significant. This way, it is easier to track the changes and to revert them if necessary. I also tried to keep the commit messages as descriptive as possible. Also, as I write this, I regret that I did not use any branching strategy, I should have used a dev branch, and a branch and merge for every feature. But well, there are so little amount of commits that it is not really a problem hard to solve from now on.

### Testing

I did small tests, only to test all the endpoints. It gives a good coverage, but the test are only happy path, with no error handling. I would like to add more tests, but I ran out of time.

## TODO

Given the limited time and scope of this project, there are many things that could be improved. Some of them are:

- loggers: Log everything, with different levels 
- metrics: metrics to monitor the application (e.g.: prometheus)
- authentication: some standard auth system for the endpoints with different roles
- error handling: better error handling for the things that FLASK does not handle
- RESTFull endpoints for all the entities
- The folder structure can be improved: A single file for each entity, and a folder for the endpoints, etc...
