## General info
Ocean API was made with Django Rest Framework

## Docs
http://localhost:8000/docs/


### How to run a project
Activate virtualenv: (venv - your virtual environment name)
```shell script
$ source venv/bin/activate
```
Install requirements:
``` shell script
$ pip install -r requirements.txt
```
To start server got to the project root and run:
```shell script
$ python3 manage.py runserver
```
To make and apply migrations run the following command:
```shell script
$ python3 manage.py makemigrations

$ python3 manage.py migrate
```
