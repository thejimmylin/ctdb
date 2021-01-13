"""
Django settings for ctdb project.

Generated by 'django-admin startproject' using Django 2.1.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# To read secrets.json
import json  # noqa
from django.core.exceptions import ImproperlyConfigured  # noqa

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured(f'Please set the "{setting}" setting in secrets_file.')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'va8k29j1o_=rs9bw!ym@s#b8zz3=9cmj_o731i$^6)9+z_9ob#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'widget_tweaks',  # this package makes it easier to integrate django templates with bootstrap
    'accounts.apps.AccountsConfig',
    'telecom.apps.TelecomConfig',
    'diary.apps.DiaryConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # for dynamic languages support
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ctdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/'), ],
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

WSGI_APPLICATION = 'ctdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES_MSSQL = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'T21',
        'USER': 'jimmy_lin',
        'PASSWORD': get_secret('DATABASES_MSSQL_PASSWORD'),
        'HOST': '10.210.31.15',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

IS_PRODUCTION = (get_secret('IS_PRODUCTION') == 'true')
if IS_PRODUCTION:
    DATABASES = DATABASES_MSSQL
else:
    DATABASES = DATABASES_SQLITE

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# We disable the AUTH_PASSWORD_VALIDATORS for convinience of users
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hant'

# For i18n
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# This limits the set_language view option
LANGUAGES = {
    ('zh-hant', ''),
    ('en', ''),
}

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')

MEDIA_URL = '/uploads/'


# build-in auth system

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'


# SMTP things
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'j3ycode@gmail.com'
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'TDB <j3ycode@gmail.com>'
SERVER_EMAIL = 'TDB <j3ycode@gmail.com>'


# Authentication things
AUTHENTICATION_BACKENDS = ['accounts.backends.AuthWithUsernameOrEmailBackend']
