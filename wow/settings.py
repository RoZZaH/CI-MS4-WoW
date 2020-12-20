import os
import environ

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
SECRET_KEY = '_$r*x_0f4mz1&ka*0#fo!84_h-1+crrm(0qhal25#tkrl6yfc2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #added, allows proper callbacks for connecting via socialaccount - try it in own project
    'django_extensions', #django shell_plus
    'allauth', #added
    'allauth.account', #added
    'allauth.socialaccount', #added
    'django_countries',
    'crispy_forms',
    # Local Apps
    "wines",
    "basket",
    "checkout",
    #'public',
    # Other
    #'crispy_forms',
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


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

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