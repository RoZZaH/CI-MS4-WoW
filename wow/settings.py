import os
import environ
import dj_database_url

#     # set casting, default value
#     DEBUG=(bool, True)
# )



# Build paths inside the project like this: BASE_DIR / 'subdir'.
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEVELOPMENT = True if os.environ.get('DEVELOPMENT') else False

if DEVELOPMENT:
    env = environ.Env()
    env_file = os.path.join(BASE_DIR, ".env")
    environ.Env.read_env(env_file)

if "DATABASE_URL" in os.environ:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = "DEVELOPMENT" in os.environ
else:
    SECRET_KEY = env("SECRET_KEY")
    DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "worldofwine.herokuapp.com"]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions', #django shell_plus
    'django.forms', #changed FORM_RENDERER
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_countries',
    'crispy_forms',
    'storages',
    # Local Apps - home is TemplateView
    # "wow.management.commands", #custom encoder/exporter - win_unicode_console error on windows 10 sys
    "wines",
    "basket",
    "checkout",
    "customers",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wow.urls'

CRISPY_TEMPLATE_PACK = "bootstrap4"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            "builtins" : [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
            'libraries': {
                'my_tags': 'templates.ttags.basket_tools',
                'helpers': 'templates.ttags.helpers',
            },
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'basket.contexts.basket_contents'
            ],
        },
    },
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # allows superusers login
    'allauth.account.auth_backends.AuthenticationBackend', #using email address, not there by default
]

SITE_ID = 1


ACCOUNT_AUTHENTICATION_METHOD = 'username_email' #allow AllAuth authenictaion using usernames or email
ACCOUNT_EMAIL_REQUIRED = True #required
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #must verify
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True #input email twice so no typos
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


WSGI_APPLICATION = 'wow.wsgi.application'


if "DATABASE_URL" in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'wow',
            'USER': env('DB_USR') if DEVELOPMENT else os.environ.get('DB_USR'),
            'PASSWORD': env('DB_PWD') if DEVELOPMENT else os.environ.get('DB_PWD'),
            'HOST': 'localhost',
            'PORT': 5432
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# AWS_s3
if "USE_AWS" in os.environ:
    #Cache
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    #Bucket
    AWS_STORAGE_BUCKET_NAME = "worldofwine"
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com" #s3-website-{AWS_S3_REGION_NAME} didn't work

    #Static and media files
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"

    #Overide static and media URLS in production
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"


# Checkout + Stripe
FREE_DELIVERY_THRESHOLD = 6
STANDARD_DELIVERY_CHARGE = 5
STRIPE_CURRENCY = 'eur'

if "DEVELOPMENT" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "hello@worldofwine.com"
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USR')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PW')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USR')

if "DEVELOPMENT" in os.environ:
    STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY') #os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
    STRIPE_WH_SECRET = env('STRIPE_WH_SECRET')
else:
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')