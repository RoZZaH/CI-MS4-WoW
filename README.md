# World of Wine - MileStone Project 4 - Code Institute


## Deployment
create venv
conda create -n hellodjango python=3.8

activate venv
conda activate hellodjango

install requirements

changed to Postgres on Windows in case features/fieldtypes unavailable in sqlite3 (e.g. listfield)
set envvars

```
set DB_USR=******
set DB_PWD=******
```

[a guide for creating django webapp on Postgres for Windows](https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294)


run initial migrations
python manage.py migrate
create a superuser 
pythong manage.py createsuperuser

requirements
django
psycopg2

python manage.py runserver (localhost:)8080

