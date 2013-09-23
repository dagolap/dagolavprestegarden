from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite'
    }
}

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1", "10.0.2.15", "10.0.2.2")

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yu2j$j&^2)@biu*z^+b)$(*m-_2)294!0@x1(uz1m^n3o*ich2'