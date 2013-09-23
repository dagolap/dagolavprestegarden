from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = get_env_variable("HOMEPAGE_SECRET_KEY")