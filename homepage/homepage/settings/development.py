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
