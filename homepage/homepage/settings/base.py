import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        raise ImproperlyConfigured("Set the %s environment variable" % (var_name, ))

# Find out what the base path for this project is so we can generate full paths based on relative paths.
PROJECT_SETTINGS_PATH = os.path.realpath(os.path.dirname(__file__))
# Root directory. Contains manage.py
PROJECT_ROOT_PATH = os.path.join(PROJECT_SETTINGS_PATH, '../..')



# Django settings for homepage project.
ADMINS = (
    ('Dag Olav Prestegarden', 'dagolav@prestegarden.com'),
)

MANAGERS = ADMINS

GRAPPELLI_ADMIN_TITLE="<a href='/'>Dag Olav Prestegarden</a>"
CRISPY_TEMPLATE_PACK = "bootstrap3"

FEED_TITLE = "Ramblings on technology and life"
FEED_URL = "http://dagolav.prestegarden.com"

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["dagolav.prestegarden.com"]


TIME_ZONE = 'Europe/Oslo'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True
USE_TZ = True



MEDIA_URL = '/media/'
STATIC_URL = '/static/'


STATICFILES_DIRS = ( # ABSOLUTE paths
    os.path.join(PROJECT_ROOT_PATH, "static"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    PROJECT_ROOT_PATH + "/templates",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'homepage.urls'
WSGI_APPLICATION = 'homepage.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',

    'grappelli',
    'filebrowser',
    'south',
    'crispy_forms',
    'rest_framework',
	'taggit',

    'apps.blog',
    'apps.portfolio',
    'apps.pages',
    'apps.comments',

    'django.contrib.admin',
    'django.contrib.admindocs',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
