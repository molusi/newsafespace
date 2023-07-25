"""
Django settings for safespace project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import cloudinary
import tinify
from pathlib import Path
import os

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import environ
import os
from dotenv import load_dotenv

from decouple import Config, Csv, config

load_dotenv()
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


SECRET_KEY = env('SECRET_KEY')
# Set the project base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
READ_DOT_ENV_FILE =env.bool("READ_DOT_ENV_FILE ",True)
if READ_DOT_ENV_FILE:
    environ.Env.read_env()
# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!

# DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
# SECURITY WARNING: don't run with debug turned on in production!

# Ver Cluster Port Status Owner    Data directory              Log file
# 12  main    5432 down   postgres /var/lib/postgresql/12/main /var/log/postgresql
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

AUTH_USER_MODEL = 'accounts.User'



# Application definition

tinify.key=env("tinify.key")


# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

cloudinary.config(
    cloud_name=config('CLOUD_NAME'),
    api_key=config('API_KEY'),
    api_secret=config('API_SECRET')
)


TINIFY_KEY = config('TINIFY_KEY')


DATABASES = {
    'default': {
        'ENGINE':env('ENGINE'),
        'NAME':env('NAME'),
        'USER':env('USER'),
        'PASSWORD':env('PASSWORD'),
        'HOST':env('HOST'),
        'PORT':env('PORT')
    }
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'crispy_forms',
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
   ]

EMAIL_BACKEND=env("EMAIL_BACKEND")
EMAIL_HOST=env("EMAIL_HOST")
EMAIL_FROM=env("EMAIL_FROM")
EMAIL_HOST_USER=env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")
EMAIL_PORT=env("EMAIL_PORT")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
PASSWORD_RESET_TIMEOUT= env("PASSWORD_RESET_TIMEOUT")





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'safespace.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'safespace.wsgi.application'




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'






MEDIA_DIR = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
