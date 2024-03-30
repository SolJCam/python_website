"""
Django settings for python_portfolio_site project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

To run Worker locally:
start redis server - 'redis-server /etc/redis/6379.conf'
start worker - python worker.py or rq worker msnbc cnn fox   - if no name options are passed as arguments, will listen to default, resulting in this worker not receiving any jobs.
start dashboard - rq-dashboard
"""


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET']
# heroku config:set DJANGO_SETTINGS_MODULE=python_portfolio_site.settings --account <your account name>
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#To run test_views in interactive interpreter (shell)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver',]

# To redirect http to https
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'py_scraper',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # heroku middleware
]

ROOT_URLCONF = 'python_portfolio_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": ["personal_portfolio/templates/", "portfolio_projects/templates/"], #should this be ["main/templates/",]?
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

WSGI_APPLICATION = 'python_portfolio_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # pip install psycopg2-binary; since updated to older working version of psycopg2=2.7.5
        'NAME': 'projects',
        'USER': 'sol',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# ------------------------------------------------------------------
#                      FOR HEROKU DEPLOYMENT
# ------------------------------------------------------------------

import os, boto3
import django_heroku
import dj_database_url # configure database - implicitly - using DATABASE_URL environ variable

# download oauth creds for email submisson from S3 bucket
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
s3_resource = boto3.resource('s3')
s3_resource.Object("portfolio-assests", "oauth2_creds.json").download_file(os.path.join(d, "../main/oauth2_creds.json"))

# path variables for local_settings.py
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(PROJECT_ROOT)

# The below variable is necessary for config['STATIC_ROOT'].        Project paths can be built using os.path.join(BASE_DIR, <filename>)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/2.2/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/staticfiles/'

# # Simplified static file serving.
# # https://warehouse.python.org/project/whitenoise/

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Allow all host hosts/domain names for this site
ALLOWED_HOSTS = ['*']

# DATABASES = { 'default' : dj_database_url.config(conn_max_age=600, ssl_require=True)}
db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# load local_settings.py
# try:
#   from python_portfolio_site.local_settings import *
# except Exception as e:
#   pass

# Activate Django-Heroku.
django_heroku.settings(locals())
