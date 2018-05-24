"""
Django settings for cms4a project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import configparser
from tools.decrypt import AESCipher
from tools.read_config import SysConfig


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = SysConfig()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'smrs95p^69t+z+)!!0g9%zoxn7m_vpr2yw)anrerhm4nxn*ssr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

LOGIN_URL = 'login'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'display_section',
    'user_section',
    'data_admin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cms4a.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cms4a.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DB_HOST = config.getValue('db', 'host')
DB_PORT = config.getInt('db', 'port')
DB_USER = config.getValue('db', 'user')
DB_PASSWORD = config.getPsw('db', 'password').decode()
DB_DATABASE = config.getPsw('db', 'database')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_DATABASE,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(processName)s:%(process)d] [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] ['
#                       '%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
#     },
#
#     'filters': {
#     },
#
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         },
#         'result': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'logs/ip_result.log',
#             'when': 'MIDNIGHT',
#             'backupCount': 7,
#             'encoding': 'utf8',
#             'interval': 1,
#             'formatter': 'standard',
#         },
#         'default': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'logs/normal.log',
#             'when': 'MIDNIGHT',
#             'backupCount': 7,
#             'encoding': 'utf8',
#             'interval': 1,
#             'formatter': 'standard',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         'request_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'logs/script.log',
#             'when': 'MIDNIGHT',
#             'backupCount': 7,
#             'encoding': 'utf8',
#             'interval': 1,
#             'formatter': 'standard',
#         },
#         'caltime_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'logs/caltime.log',
#             'when': 'MIDNIGHT',
#             'backupCount': 7,
#             'encoding': 'utf8',
#             'interval': 1,
#             'formatter': 'standard',
#         },
#     },
#
#     'loggers': {
#         'django': {
#             'handlers': ['default'],
#             'level': 'INFO',
#             'propagate': False
#         },
#         'django.request': {
#             'handlers': ['request_handler'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'heartbeat': {
#             'handlers': ['heartbeat'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#         'caltime': {
#             'handlers': ['caltime_handler'],
#             'level': 'INFO',
#             'propagate': True
#         },
#     }
# }
