# World of Wine - MileStone Project 4 - Code Institute

## User Stories

### View and Navigate Store
- User viewa list of products(wines)
    -- select some for purchase (DetailView)
- View Individual Product details
    -- view product/wine description and details (DetailView)
- User can identify deals/clearance items (??)
    -- take adavnateg of special offers
- User can easily view total of their purhcasers
    -- avoid overspend

### Registration and User Account
User and Customer used interchangeably here
Owner and Admin likewise mean Site Owner/Administator
- Users can easliy register for an account (using AllAuth)
    -- have personal account and able to view profile (user app)
- User can easily login/logout (using AllAuth)
    -- access personal account info (user app)
- User can easily recover password
    -- recover access to their account
- User has a personalised account area
    -- user can view previous order history and change their details (user app)

### Product/Wine Sorting and Searching

### Purchasing and Checkout


## Deployment
create venv
conda create -n wow python=3.8

activate venv
conda activate wow





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

## Requirements (Package Management)
- django
- psycopg2 (for postgres on windows/localhost and heroku/production)
- allauth (pip install django-allauth)
- django extensions (shell plus) (pip install django-extensions)

pip freeze > requirements.txt

python manage.py runserver (localhost:)8080

