<h1 id=top align=center>World of Wine - MileStone Project 4 - Code Institute</h1>

##OVERVIEW
World of Wine is a speculative e-commerce website for an online wine merchant; using Django, Postgres and Stripe. 

View live demo is deployed on [heroku](https://worldofwine.herokuapp.com/) ; please be patient while the free dyno spins up.

##[Table of Contents](#table-of-contents)


1. [User Experience](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
2. [Wireframes](#wireframes)
3. [Features](#features)
  - [Existing Features](#existing-features)
    - [Features On All Pages](#features-on-all-pages)
    - [Features Of Individual Pages](#features-of-individual-pages)
  - [Features Left To Implement](#features-left-to-implement)
4. [Technologies Used](#technologies-used)
  - [Front-End Technologies](#front-end-technologies)
  - [Back-End Technologies](#back-end-technologies)
  - [Other Tools](#other-tools)
5. [Testing](#testing)
6. [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Remote Deployment](#remote-deployment)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)

---
##USER EXPERIENCE UX
###User Stories

####As a customer, I want to be able to:
- Easily register for a user account, so that I can login/logout of the site securely and reset my password easily.
- Store or update some of my personal information in my account profile to save me having to fill out delivery details each time. 
- Have a personalised user account so that I can view my personal order history, order confirmations and payments made.
- Easily browse quality wines by type (Red, White etc.) and ratings, 5-star ratings and [Parker points](https://www.robertparker.com/about/ratings)
- Easily drill down to a detailed view of a wine I am interested in to find out more

####As a staff member, I want to be able to:
- Easily add new products to sell, so that I can keep the site reflecting new wines in stock.
- Easily edit/update existing products that are listed, so that I can keep the wine listings up to date
- Delete and remove wines that are no longer available to avoid shopper disappointment / frustration. 
- Easily view a list and sort of a list of wines in the backend system to see wines currently discounted. 

####As a causal shopper, I want to be able to:
- Search the website for a particular wine or wine region.
- Easily add a wine to my cart/basket
- Easily adjust the quantity of a particular wine (line item) or remove the item entirely from my basket
- See the subtotal for each item, so that I can see how much I am spending on each item 
- Safely and securely use my card details via the Stripe payment gateway to make a purchase
- View an order confirmation, and receive an email after checkout so that I know the order went through.

[Back to TOC](#toc)
---


### Product/Wine Sorting and Searching

### Purchasing and Checkout


### Testing and Bugs






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

