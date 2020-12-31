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
    - [Current Features](#current-features)
      - [Site-wide Features](#site-wide-features)
      - [Features Of Individual Pages](#features-of-individual-pages-django-apps)
    - [Future Features](#future-features)
4. [Technologies](#technologies)
    - [Web Technologies and Frameworks Used](#web-technologies-and-frameworks-used)
    - [Coding Choices](#coding-choices)
5. [Testing and Bugs](#testing-and-bugs)
    - [Manual Tests](#manual-tests)
    - [Automated Tests](#automated-tests)
    - [Visual Tests](#visual-tests)
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
- Dark Burdundy <span style="color:#46001A display:inline-block; height:10px; width:10px"></span> (hex &num;46001a)
- Lighter Wine <span style="color:#6E032A display:inline-block; height:10px; width:10px"></span> (hex &num;6e032a)

along with <span style="color:#000000; display:inline-block; height:10px; width:10px"></span> Jet-Black (hex &num;000000) for some text-elements.


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
 - I decided to use **Postgres** on Windows for my database in case features I may wish to use that are unavailable in sqlite3 (e.g. listfield or aggregations) it also will hopefully allow for smoother deployment as this is the default setup on Heroku. I followed this short Medium article by [9cv9](https://9cv9.com/) for [creating django webapp on Postgres for Windows](https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294) 
- Payments are handled via the [**Stripe**](https://stripe.com) payments system and API mostly using [JQuery](https://jquery.com/) as a convenience; there are some traces of vanilla <abbr title="Ecmascript 6">ES6</abbr> but I'd love to see if the javascript could be handled by something like Alpine.js. 

### Coding Choices
Where possible I tried to implement **Class-based Views** in Django, following the approach advocated by Daniel & Audrey Feldroy, authors of [Two Scoops of Django
](https://www.feldroy.com/); I had implemented function based views in my Milestone 3 Flask project and the terse code and logical defaults appealed. Django is, however, a large framework so I didn't deviate too much from standard <abbr title="Create Read Update Delete">CRUD</abbr> functionality and some signals.

During development, I also decided to centralise the app templates, 'includes' and form widgets. I found it much easier to work like this even if it meant some extra setup in the settings file. Files are easily understood as belonging to a particular app by their prefix. In future I would like to recode this project in Tailwind on the way to turning chunks into components; and utlimately code a Vue App that talks to a Flask or Django REST API.

[Back to TOC](#table-of-contents)
---
## TESTING AND BUGS

### Manual Tests
Given that this final project has e-commerce functionality at it's heart once I was satisified that orders where being correctly recorded into the overall Order and Order Lineitems I worked with the [StripeCLI to test webhook](https://stripe.com/docs/stripe-cli/webhooks) functionality; this means that an order is created as a fallback where a payment-intent succeeds but no order yet exists in  the database. If using localhost you have to authenicate via the StripeCLI `stripe login` and it opens a browser to login similar to Github in VSCode or HerokuCLI.
`stripe listen --forward-to localhost:8080/checkout/wh/`

![](/docs/stripe-webhooks.png)
Event Logs from Stripe show webhooks (and payment intents) succeeding locally but payment_intent.succeeded not on the deployed Heroku App; interestingly any other webhooks are handled generically and payment_intent.payment_failed also works sending from the Stripe dashboard. This may be the reason no confirmation emails are being sent from the deployed app while AllAuth signup does work (sending from hello.worldofwine@gmail.com).

### Automated Tests
I fully intended to write some automated tests as outlined in the Django Crash Course but I knew using data factories like [Factory Boy](https://factoryboy.readthedocs.io/) had the potential to pollute my database so I decided to back it up before writing and testing functions **assert url** based on a saved concantenated slug but I unfortunately ended down a cul-de-sace in that my windows console was choking writing out unicode characters to json. I tried everything changing the font, writing a custom dumpdata command (see wow.management.commands) before having to install win_unicode_console and setting a PYTHONIOENCODING=utf-8
Ideally I would have devised a test for each required field and also calculations for free delivery and checkout and this maybe where the 'magic' of Class-based Views obscured the fundamentals of Testing Driven Design.


### Visual Tests
The site has been well tested for responsiveness although I have found that when developing locally Developer Tools (in Chrome and Firefox) seem to open / initate a click event on the mobile navigation and suddenly the layout breaks - even the mobile navigation. However with Devloper Tools closed or behaving the layout wraps as intended.



[Back to TOC](#table-of-contents)
---
## DEPLOYMENT

### Local Deployment

In order to run/review this project locally you will need to you have the following software in place:

Prerequisites:
- Python 3
- PIP
- GIT
- Local Postgres Database (incl for Windows)
- Stripe (Testing) Credentials
- StripeCLI


1. Ensure you have [Python 3](https://www.python.org/downloads/), [PIP](https://pip.pypa.io/en/stable/) Package Manager, and [Git](https://git-scm.com/) installed, using command-line/terminal on your computer.

1. This project uses a Postgres database for local development; for Windows installation [please see this article](https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294) . It's best to use an admin login of **postgres** and a password that you can remember / write down for database admin and creating the django superuser.

1. Create a Virtual Environment using **venv**, [**pipenv**](https://realpython.com/pipenv-guide/), **virtualenv** or [**anaconda**](https://docs.conda.io/en/latest/miniconda.html#windows-installers)

1. Depending on your computer os change the commands as appropriate (Mac tends to also have Python 2 installed so you need to use pip3 or python3 in your commands)<br>
  - 
	```
	python3 -m venv wow
	source wow/bin/activate #to activate
	```
	
 - or use `pipenv shell` if using pipenv

 - or<br>
	```
	create venv
	conda create -n wow python=3.8
	
	activate venv
	conda activate wow
	```

1. usually the pip version is outdated install old version of pip
    `pip install --upgrade pip`

1. Clone the Git Repo<br>
    if using [VSCode](https://code.visualstudio.com/) Ctrl+Shift+P (Win) or Cmd+Shift+P (Mac) type 'Clone' (Git:Clone)<br>
    * Paste in this Git URI -> https://github.com/RoZZaH/CI-MS4-WoW

1.  use the requirements.txt to install dependicies <br>
N.B. if deploying to heroku uncomment the line for gunicorn<br>
`pip install -r requirements.txt` or alternatively `pipenv install requirements.txt`

1. [Stripe](https://stripe.com/en-ie) credentials - specifically a Stripe Public Key and a Stripe Secret Key - are needed in order to test the checkout functionality, - to be put in a .env file or local environemnt varaiables (see below).
N.B. you will not need AWS S3 Buckets setup for local development/review

1. The requirements file should have install [django-environ](https://django-environ.readthedocs.io/en/latest/)<br>
Create an .env file with the following credientals / string values (no need for quotation marks after the equals (=) sign)

```
DB_USR=postgres
DB_PWD=[password used to set up postgres or specific app database]
SECRET_KEY=[Django secret key, paste from settings.py or generate your own]
STRIPE_PUBLIC_KEY=[Testing Public API key]
STRIPE_SECRET_KEY=[Testing Secret key - this key type should definitely be kept out of source control]
STRIPE_WH_KEY=[Testing Webhook Api Secret Key - again never in source control]
EMAIL_HOST_USER=[an email address configured for SMTP / low security sending]
EMAIL_HOST_PASS=[password for above email address - must be kept out of source control]
```

1. You will also need to set an environmental variable for DEVELOPMENT=True
- `set DEVELOPMENT=True'` on Windows
- `export $env:DEVELOPMENT='True'` in Powershell (Windows)
- `export DEVELOPMENT=True` on Mac/Unix

1. Migrate the initial Django models using :
- `python manage.py migrate`
 
1. You will should *NOT* need to create a superuser as the *fixture*/backup should load in some users:
- `python manage.py loaddata db.json`

1. This should be everything & your site should be running correctly now. You can run the project using
- `python manage.py runserver <localhost><port e.g. 8080>`

[Back to TOC](#table-of-contents)
---

### Remote Deployment

Prerequisites:
  - Python 3
  - PIP
  - GIT
  - Heroku account and HerokuCLI
  - Stripe (Testing) Credentials
  - (optional : AWS / S3 Bucket - not required for functionality)

1. (Sign up) Login into your Heroku account 
2. Create a new app, called <appname>, selecting the location nearest to you - i.e. Europe. 
3. Under the ‘Resources’ tab, search for and add the ‘Heroku Postgress DB’ app
4. In the project terminal, install `dj_database_url`, `psycopg2` by using the following commands: 	
    1. `pip install dj_database_url`
    2. `pip install psycopg2-binary`
    3. also install `pip install gunicorn` it will be needed for deployment later on
  
5. Next, freeze these requirements into a requirements file Heroku will use to install the necessary packages for deployment
- `pip3 freeze > requirements.txt`
6. To populate the remote heroku (postgres) database you can:
    1.  Comment out the current `DATABASE` settings (we will need them again later), and add:
	- ‘Default’: dj_database_url.parse(<new Database_URL here>)
    2. import the DJ database connector inserting `import_dj_database_url` at the top of the **settings.py**  file
    3. On Heroku site Go to your <app> under Settings > Reveal Config Vars > DATABASE_URL
    4. Add the Heroku this **postgres://** URL into brackets as follows `dj_database_url.parse.parse(<database_url>)` 
	
7. Now run all the migrations to get our database set up: 
    1. `python3 manage.py migrate`
    2. `python manage.py loaddata db.json`
    3. You should **not** need to create a superuser; but that command is `python manage.py createsuperuser` if you do.
  
8. Run the django server (locally) `python manage.py runserver <localhost:port>` and you should notice a slight lag as you connect to the remote database.
9. Before commiting anything to GIT **remove the new dj_database_url settings** and uncomment out the original settings so they are re-eanbled. This stops the database URL going into version control. Alternatively you could have added the remote db as an environmental variable (to for example django-environ) to be safer.
10. Edit the django **settings.py** file with an if statement, looking for DATABASE_URL, the Heroku variable otherwise connect to the local Postgres server. 
11. Create a Procfile to tell Heroku to create a web dynamo, which will run unicorn and serve or Django app
12. Add the following to your Procfile 
  - `web: gunicorn wow.wsgi:application`
13. Log into HerokuCLI via the terminal with the following command: 
  - `heroku login -i`
14. Temporarily disable collect static using the following command: 
  - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <appname>`
15. In settings.py, updated the `ALLOWED_HOSTS` settings. `Localhost` allows Local Development or Gitpod to still work too 
  - ALLOWED_HOSTS = ['<appname>.herokuapp.com', 'localhost']
16. add git remote for heroku and push there
  - `git remote add heroku https://git.heroku.com/<project-name>/git`
17. Commit all and push to the new remote
  - `git push heroku <master||deploy-branch>`
    1. In Heroku, you can connect to a Github Repo (you'll be asked to authenicate access) and even a branch; you can set Enable/Disable 'Automatically Deploy'; there is also options to work with <abbr title="Continuous Improvement">CI</abbr> tools like Travis.
18. Static and Media Folders and URLs are set up using AWS s3 Buckets which is more involved and beyond the scope of this readme; see the **settings.py** file for an idea as to how this works - you'll need to install 2 new packages **django-storages** and **boto3** ; this [article](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html) may also help.
19. In Order to get **Stripe** to work you will need to set the following variables:
    - ![](/docs/heroku-envvars.png)
    - this is very similar to environmental variables used in the local deploy above

[Back to TOC](#table-of-contents)
---

## Credits

### Media
- [Landing Page Background](https://unsplash.com/photos/x5O1GmmGoPE) from [Unsplash](https://unsplash.com/) by [Chuttersnap](instagram.com/chuttersnap)

- The majority of the product images were from [Vinino](https://www.vivino.com/) which provides services like wine product data and images via API

### Content
- The product details were gleaned from [Robb Report](https://robbreport.com) best wines reports and cross referenced with images from [Vivino](https://vivino.com) and details from [Wine Searcher](https://www.wine-searcher.com/); I aggregated info in excel and then exported to csv and used column select to add json tags for import as a fixture into Django

### Code

- The wine/products and checkout apps of the course was adapted from the [Boutique Ado Mini Project](https://github.com/ckz8780/boutique_ado_v1/) from the [Code Institute](https://codeinstitute.net/) Full Stack Developer course; which I tried make my own by using Classes/Class-based Views as appropriate.
- I bought a copy of Daniel and Audrey Feldroy's [*A Wedge of Django (a crash course)*](https://www.feldroy.com/) and also referred an older version of [Two Scoops of Django](https://www.feldroy.com/) when the [Django Docs](https://docs.djangoproject.com/en/3.1/) got the better of me
- [Very Academy](https://twitter.com/VeryAcademy) has a fantastic playlist on Youtube covering [**Class-based Views**](https://www.youtube.com/playlist?list=PLOLrQ9Pn6caxNb9eFZJ6LfY29nZkKmmXT) in Django 

---

## Acknowledgements

I would like to thank the [Code Institute](https://codeinstitute.net/), and particularly Mark McCann, for assisting me in completing the course;<br>
my mentor, Aaron Sinnott, a fellow Wexford man was also great guide during a difficult year [2020].

[Back to TOC](#table-of-contents)
---
