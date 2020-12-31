<h1 id=top align=center>World of Wine - MileStone Project 4 - Code Institute</h1>

## OVERVIEW
World of Wine is a speculative e-commerce website for an online wine merchant; using Django, Postgres and Stripe. 

View live demo is deployed on [heroku](https://worldofwine.herokuapp.com/) ; please be patient while the free dyno spins up.

## [Table of Contents](#table-of-contents)


1. [User Experience](#user-experience-ux)
    - [User Stories](#user-stories)
    - [Design](#design)
      - [Imagery](#imagery)
      - [Typography](#typography)
      - [Iconography](#iconography)
      - [Colour Scheme](#colour-scheme)
2. [Wireframes](#wireframes)
3. [Features](#features)
    - [Existing Features](#existing-features)
      - [Features On All Pages](#features-on-all-pages)
      - [Features Of Individual Pages](#features-of-individual-pages)
    - [Features Left To Implement](#features-left-to-implement)
4. [Technologies](#technologies-used)
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
## USER EXPERIENCE UX
### User Stories

#### As a customer, I want to be able to:
- Easily register for a user account, so that I can login/logout of the site securely and reset my password easily.
- Store or update some of my personal information in my account profile to save me having to fill out delivery details each time. 
- Have a personalised user account so that I can view my personal order history, order confirmations and payments made.
- Easily browse quality wines by type (Red, White etc.) and ratings, 5-star ratings and [Parker points](https://www.robertparker.com/about/ratings)
- Easily drill down to a detailed view of a wine I am interested in to find out more

#### As a staff member, I want to be able to:
- Easily add new products to sell, so that I can keep the site reflecting new wines in stock.
- Easily edit/update existing products that are listed, so that I can keep the wine listings up to date
- Delete and remove wines that are no longer available to avoid shopper disappointment / frustration. 
- Easily view a list and sort of a list of wines in the backend system to see wines currently discounted. 

#### As a causal shopper, I want to be able to:
- Search the website for a particular wine or wine region.
- Easily add a wine to my cart/basket
- Easily adjust the quantity of a particular wine (line item) or remove the item entirely from my basket
- See the subtotal for each item, so that I can see how much I am spending on each item 
- Safely and securely use my card details via the Stripe payment gateway to make a purchase
- View an order confirmation, and receive an email after checkout so that I know the order went through.

### Design

World of Wine was designed with functionality and ease of use in mind, the design has been kept simple but strong, to engender the idea of stability and trust in the brand. The design uses a subtle colour-palette maintaining the focus being on high quality product images, and well understood design language of an ecommerce website, logo, navbar, icons for basket, profile, cards, detailed view and buttons and form fields.

This project was aimed at wine lovers, who want to find great wine to suit their own taste and style. The homepage shows an image of a selection of sample bottles and crates demostrating of a clicks-and-bricks established wine merchant; with a call to action for browse the store.

#### Imagery

High Quality Product Shots are the primary focus - these were sourced from [Vivino.com](https://vivino.com) , who are a marketplace aggregator, but also provide paid API services including product shots. The cover image on the homepage is by [Chuttersnap](instagram.com/chuttersnap) on [Unsplash](https://unsplash.com/photos/x5O1GmmGoPE)


#### Typography
An elegant pairing of serif (Droid-Serif) and sans-serif (Lato) fonts were used in keeping with the tradition and sophisication of wine as a premium product.
Care was taken to ensure legibility of each wine's attributes with headings in different weights and italics.

#### Iconography
Subtle icons from Font-Awesome and Icons8 along with CountryFields flags option help lift the design and break the text into logical attributes.

#### Colour Scheme
In keeping with the concept and market for an online wine merchant, World of Wine is a simple sophisicated design with some subtle gradients in the footer and delivery banner. 

So, the three main colours seen are: 
- White
- Dark Burdundy (hex &num;46001a)
- Lighter Wine (hex &num;6e032a)

along with Jet-Black (hex &num;000000) for some text-elements.


[Back to TOC](#table-of-contents)
---

## WIREFRAMES


[Back to TOC](#table-of-contents)
---


## FEATURES

### Current Features 

#### Site-wide Features

##### Navigation
- The responsive header contains four main navigation sections:
	- The World of Wine logo links back to the home/landing page.
	- A Search Form
	- The main cross-site navigation - principally wine types/categories
	- An Account Icon with a dropdown to Profile Page containing their primary delivery address and order history or the option to log out, once logged out the options change to Register or Login. If the user a staff member (supervisor), they can add products but also will see options to edit and delete products in the card and detail views; their is also a confirmation step in the deletion process. 
	-  The Shopping Basket/Cart Icon shows the current total.
- The wines list view also has product sorting so shopper can order and categorise wines by type, rating and price.

##### Order Offer 'strap'
- Under the main navigation is a conditional marketing banner/strap highlighting the offer of free delivery on purchase of 6+ bottles.
 
##### Footer 
- A site footer includes potential links to the social media accounts, copyright information, site policies such as privacy notice and order processing rules and refund information, along with future information pages about the shop.

#### Features of Individual Pages (Django Apps)

##### Home Page 
- The home/landing page shows an image of a selection of sample bottles and crates giving the impression of a clicks and bricks wine merchant; with a call to action for browse the store.

##### Wine Product Pages
- The wine listing page allows users to filter and order wine by type, price, or rating. Users can click on the bottle product shot to get a detailed view. 
- Staff and superusers can update the details of a product easily either edit or delete existing products or add new wines via the create form.
- Product Deletion has some defensive design with a confirmation page/step before completion.

##### Basket Page
- Customer can adjust the quantity the quantity of the wine they are ordering and see updated totals for the products subtotal and overall total.
- Customer can remove an item from their basket easily.

##### Customer Page 
- Users can navigate to their Profile page via the Account icon. This page allows them edit/update their delivery address. Users also see a recent order history.

##### Checkout
- Checkout pre-fills their delivery address and details from a combination of their User and Customer data, and allows payment using the [Stripe](https://stripe.com/) payment gateway. Once the order has been completed and payment has been processed, the user will receive an email confirmation; this happens even if the customer closes their session or browser via the Stripe Webhooks API, the system checks to see if a payment intent has an order associated with it and if that times out it generates one, completing the process, sending a confirmation email and clearing the basket.

### Future Features

Bulk purchasing and discounting could really be investigated will tiered discounts based on the number of cases, rather than bottles, customers buy. That moves the site beyond a consumer one to more a commercial wine merchants supplying local restaurants and events companies.

There many features one could implement to extend the value and stickiness of an online wine merchant:

 - Social Media Login: Allowing users to log via their social account such as Facebook or Google would ease the friction at the sign-up stage.
 - Curate customer or expert  reviews of various wines to help customers become a community 
 - Wine Pairing - categorise wines based on what food they pair well with.
 - Wine Style - categorise wines based on 'style' or palette.

[Back to TOC](#table-of-contents)
---
## TECHNOLOGIES
### Web Technologies and Frameworks Used

 - This project uses **[Django](https://www.djangoproject.com/)**, a framework built on top of Python to ease development of projects using the <abbr title="Model View Template">MVT</abbr> pattern to build Database-agnostic Models, Views and Templates, temaples using the jinja templating language with {{handlebar syntax}} for inserting dynamic 'context-data' into html pages.
 - Configuration for installed apps and features use the **settings.py** file in a 'core' or main project app   
 - **static files** for <abbr title="Cascading Style Sheets">CSS</abbr> and Javascript files are pointed to using the **load static** method; [Bootstrap](https://getbootstrap.com) was used as the CSS framework; I plan to rewrite this using *Tailwind* in future.
 - **media** files such as images can reside in local folders or using **<abbr title="Amazon Web Services">AWS</abbr> Buckets** as deployment takes place on [**Heroku**](https://heruko.com) free-tier hosting and dynos spin up when the app is requested but it has 'ephemeral storage' meaning uploads like images would disappear once a dyno winds down and resets to the deploy state.
 - Apps and data migrations are added using functions from the **manage.py** file and django shell
 - I decided to use **Postgres** on Windows for my database in case features I may wish to use that are unavailable in sqlite3 (e.g. listfield or aggregations) it also will hopefully allow for smoother deployment as this is the default setup on Heroku.
I followed this short Medium article by [9cv9](https://9cv9.com/) for [creating django webapp on Postgres for Windows](https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294) 
 - Where possible I tried to implement **Class-based Views** in Django, following the approach advocated by Daniel & Audrey Feldroy, authors of [Two Scoops of Django
](https://www.feldroy.com/); I had implemented function based views in my Milestone 3 Flask project and the terse code and logical defaults appealed. Django is, however, a large framework so I didn't deviate too much from standard <abbr title="Create Read Update Delete">CRUD</abbr> functionality and some signals.
- Payments are handled via the [**Stripe**](https://stripe.com) payments system and API mostly using [JQuery](https://jquery.com/) as a convenience; there are some traces of vanilla <abbr title="Ecmascript 6">ES6</abbr> but I'd love to see if the javascript could be handled by something like Alpine.js. 


[Back to TOC](#table-of-contents)
---



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

