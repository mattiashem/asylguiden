# Django settings for asylguiden project.

import os
import mandrill

MAINDRILL_API='AJnSnqZGRKCLQKMQoiMUbA'
MAINDRILL_API='AJnSnqZGRKCLQKMQoiMUbA'
TWITTER_APP_KEY = '5tFF4zrutyd41NvRf7MLeD0Lk'
TWITTER_APP_SECRET = 'k21rq1Df3grADRtrIYDTe6lBuUGY4CK5E3V00t9YU259A2yCQ9'
TWITTER_APP_ACC_TOK = '2703914418-69pwELq0Eb7D6U8RcMzjlnHgybz4Yg9tBOGg2cv'
TWITTER_APP_ACC_SEC = 'KiDwoCJ43xAAE6krIA5HYPdEFqBKbDFdzDHQHsermbRHH'
FACEBOOK_PAGE_ID = "175357059145044"
FACEBOOK_ACCESS_TOKEN =  "CAAMjjvZCa5L4BAJRdmPf9xx5kACHOnCjs9ZCy38oQkIWj4BlfMGp4E2Lj1kZB2wffajaZAXjCTlgymAsFVr5g1bFYucVrFpBExmDkgkxyvaCZA3dXzBZBriVNW03F1UtPx8T8VhSuGDLdfGy5JG3ZCMZCXYPTZCclwX3gAL1ikqPpdEZCduHNTAWNIZCKBMJvzR5ELcdGzrVq1nGVovalp2j7TZB"


ALLOWED_HOSTS = ['localhost', '127.0.0.1','www.asylguiden.se','asylguiden.se']

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = True

#connect('guide',host='mongo')

ADMINS = (
     ('Mattias', 'mattias@asylguiden.se'),
)

#THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
THUMBNAIL_STORAGE = '/code/static/thumb'


#FILEBROWSER_DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

#AUTHENTICATION_BACKENDS = (
#    'mongoengine.django.auth.MongoEngineBackend',
#)

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

MANAGERS = ADMINS

BASE_DIR ='/code/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"), # Assuming BASE_DIR is where your manage.py file is
)




DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'guide',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'mongo',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = '/code/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = '/code/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
#STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/home/mattias/projects/asylguiden/static'
#)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3zhjdhWLwdwDWDW!12334&45690sdfSDFSDFDFSDFS'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

#     'django.template.loaders.eggs.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request",



)




MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)


ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('sv', ugettext('Swedish')),
    )




ROOT_URLCONF = 'asylguiden.urls'

TEMPLATE_DIRS = (
	'/code/template',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'edu',
    'work',
    'book',
    'users',
)




#DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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
