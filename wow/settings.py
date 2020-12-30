import os
import environ
import dj_database_url

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
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
    # Local Apps
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
            # os.path.join(BASE_DIR, 'venv/lib/site-packages/django/contrib/admin/templates' )
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'loaders' : [
            #     ('django.template.loaders.filesystem.Loader',
            #     [BASE_DIR / 'templates'],)
            # ],
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
                'django.template.context_processors.request', #req by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'basket.contexts.basket_contents'
            ],
        },
    },
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

# MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # allows superusers login
    'allauth.account.auth_backends.AuthenticationBackend', #using email address, not there by default
]

SITE_ID = 1

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

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
        'default': dj_database_url.parse('postgres://zgatftjzgmwwzr:59703e1955508d481f37f86964780937640120ea310ccfe9eabc12e6e5ea9c69@ec2-46-137-123-136.eu-west-1.compute.amazonaws.com:5432/d5mjoi57dgh2ki')
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'wow',
            # 'USER': os.environ.get('DB_USR'),
            'USER': env('DB_USR'),
            # 'PASSWORD': os.environ.get('DB_PWD'),
            'PASSWORD': env('DB_PWD'),
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

FREE_DELIVERY_THRESHOLD = 6
STANDARD_DELIVERY_CHARGE = 5
STRIPE_CURRENCY = 'eur'
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY') #os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = env('STRIPE_WH_SECRET')
WOW_CONTACT_EMAIL = "hello@worldofwine.com"