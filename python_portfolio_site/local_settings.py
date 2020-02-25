'''
By adding a local_settings.py file, you can extend the settings.py file with settings relevant to your local environment, 
while the main settings.py file is used solely for your staging and production environments. 
'''

from python_portfolio_site.settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    # 'default': {},
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # pip install psycopg2-binary; since updated to older working version of psycopg 2.7.5
        'NAME': 'projects',                      
        'USER': 'Sol',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    },
    # 'dictionary': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'dictionary',                      
    #     'USER': 'Sol',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
}