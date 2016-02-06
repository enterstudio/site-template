"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django {{ django_version }}.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '5(15ds+i2+%ik6z&!yer+ga9m=e%jcsadqiz_5wszg)r-z!2--b2d')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

APPS = []

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'leonardo'),
        'USER': os.environ.get('DB_USER', 'leonardo'),
        'PASSWORD': os.environ.get('DB_PASS', 'leonardo'),
        'HOST': os.environ.get('DB_SERVICE', 'postgres'),
        'PORT': os.environ.get('DB_PORT', 5432)
    }
}


# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.environ.get('STATIC_ROOT', "/var/lib/leonardo/static")
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', "/var/lib/leonardo/media")

SITE_ID = 1
SITE_NAME = '{{ project_name }}'

# redirect migrations
MIGRATION_MODULES = {
    'web': 'leonardo_site.migrations.web',
}
