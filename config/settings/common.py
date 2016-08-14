# @Author: Hodonou SOUNTON <drxos>
# @Date:   2016-08-14T01:52:31+01:00
# @Email:  sounton@gmail.com
# @Project: djangoku
# @Last modified by:   drxos
# @Last modified time: 2016-08-14T02:37:37+01:00
# @License: Copyright (c) 2016 The MIT License (MIT)


"""
Django settings for config project on Dokku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

import os
import environ
import dj_database_url


# Getting the root and apps directories
# -----------------------------------------------------------------------------
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('zbraa')

# Getting environ instance
# -----------------------------------------------------------------------------
env = environ.Env()

# .env invocation
# -----------------------------------------------------------------------------
environ.Env.read_env(env_file=ROOT_DIR()+'/.env')

# DEBUG
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', False)

# SECRET CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGEME!!!')

# Application definition
# -----------------------------------------------------------------------------
### Django basic applications
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
)

### Vendor applications
VENDOR_APPS = (
    'django_extensions',
)

### Local applications
LOCAL_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + VENDOR_APPS + LOCAL_APPS

# MIDDLEWARE CLASSES and ROOT_URLCONF
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

# TEMPLATES
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ROOT_DIR('templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

# WSGI APPLICATION
# -----------------------------------------------------------------------------
WSGI_APPLICATION = 'config.wsgi.application'

# Database configuration
# -----------------------------------------------------------------------------
### https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
        # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
        'default': env.db('DATABASE_URL', default='postgres:///zbraa'),
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

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
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# FIXTURE
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Porto-Novo'

# Static adn media files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = str(ROOT_DIR.path('staticfiles'))
STATIC_URL = '/static/'

MEDIA_ROOT = str(ROOT_DIR.path('media'))
MADIA_URL = '/media/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]
