from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

FEED_TITLE = "Ramblings on technology and life"
FEED_URL = "http://dagolav.prestegarden.com"

STATIC_ROOT = get_env_variable("HOMEPAGE_STATIC_ROOT")
MEDIA_ROOT = get_env_variable("HOMEPAGE_MEDIA_ROOT")

SECRET_KEY = get_env_variable("HOMEPAGE_SECRET_KEY")

