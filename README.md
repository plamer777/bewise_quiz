# The Bewise-Quiz API
The API allows to get and save a certain amount of questions uploaded from external service.

The app provides functionality as follows:
 - To get and automatically save from one question to any amount you want (all questions are unique)
 - To get last previously saved question 
 
---

**Technologies used in the project:**
 
 - Flask
 - Flask-RESTX
 - SQLAlchemy 
 - Gunicorn
 - Poetry
 - Pydantic
 - Docker
 - Docker-compose

---

**Project's structure:**
 
 - dao - data access objects to work with database
 - services - service objects with business logic
 - setup - initialization of the SQLAlchemy and Flask-RESTX
 - views - class based views to process requests
 - configs.py - Flask configuration object
 - constants.py - constants to configure the application
 - container.py - DAO and Service instances
 - Docker-compose.yaml - main file to start the application by using Docker
 - Dockerfile - description of the image to create API container
 - init_app.py - creation and configuration of the application
 - main.py - file with Flask application to start
 - utils.py - utility functions
 - README.md - this file with project description
---

**How to start the project:**
The app is ready to install out of the box. There are two containers in the docker - db providing database and
api with the application.
To start the app just follow the next steps:
 - Clone the repository
 - Install docker and docker-compose packages by the command `sudo apt install docker.io docker-compose`
 - Prepare .env file using an example provided below
 - Prepare docker-compose.yaml file (change settings such as ports, images if you need)
 - Start the app by using `sudo docker-compose up -d` command
 - The main page with swagger will be available by the url http://localhost/ (if started locally) or http://yourdomain/ 
(if started on the server)
 - After that application is ready to process requests

---

**An example of request:**

- POST: http://localhost/tasks/add/
- json: {"question_num": 2}
- responses:
1. first time:
`
    {
      "id": null,
      "question": null,
      "answer": null,
      "created_at": null,
      "value": null
    } `
2. every next time:
`    {
      "id": 2,
      "question": "In 2012 it became the first school to have players go 1-2 in the NBA draft--Anthony Davis & Michael Kidd-Gilchrist",
      "answer": "the University of Kentucky",
      "created_at": "2022-12-30T21:20:30.241000",
      "value": 800
    }`

---
Example of .env file:

    POSTGRES_DB=booking - your db name
    POSTGRES_PASSWORD=plamer0805 - db username's password
    POSTGRES_USER=plamer - db username
    POSTGRES_PORT=5432 - db port
    POSTGRES_HOST=db - database host (the name of docker container)
    CLEAR_DB=True - if True then all tables will be deleted each time you start the application
    API_VERSION=1.0.0 - current API version (all three settings used only for swagger)
    API_TITLE=Bewise Quiz API - API title
    API_DESCRIPTION=This API allows you to save unique questions for quiz in database - API description


The project was created by Alexey Mavrin in 27 May 2023