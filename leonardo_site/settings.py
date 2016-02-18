"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django {{ django_version }}.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', '5(15ds+i2+%ik6z&!yer+ga9m=e%jcsadqiz_5wszg)r-z!2--b2d')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

APPS = []


def test_connection():
    """Test whether the postgres database is available
    """
    import socket

    try:
        s = socket.create_connection(
            (os.environ.get('DB_SERVICE', 'postgres'), 5432), 5)
        s.close()
    except socket.timeout:
        msg = """Can't detect the postgres server. If you're outside the
        intranet, you might need to turn the VPN on."""
        raise socket.timeout(msg)

try:
    test_connection()
except Exception as e:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('DB_SERVICE', 'postgres') + ':11211',
        'TIMEOUT': 120,
        'KEY_PREFIX': 'LEONARDO'
    }
}
# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Openstack Swift Storage
# https://github.com/blacktorn/django-storage-swift
DEFAULT_FILE_STORAGE = 'swift.storage.SwiftStorage'
SWIFT_AUTH_URL = os.environ.get('SWIFT_AUTH_URL', 'http://10.0.170.10/v2.0')
SWIFT_AUTH_VERSION = os.environ.get('SWIFT_AUTH_VERSION', 2)
SWIFT_USERNAME = os.environ.get('SWIFT_USERNAME', 'swift')
SWIFT_KEY = os.environ.get('SWIFT_KEY', 'swift')
SWIFT_TENANT_NAME = os.environ.get('SWIFT_TENANT_NAME', 'service')
SWIFT_USER_DOMAIN_NAME = os.environ.get('SWIFT_USER_DOMAIN_NAME', 'default')
SWIFT_PROJECT_DOMAIN_NAME = os.environ.get(
    'SWIFT_PROJECT_DOMAIN_NAME', 'default')
SWIFT_CONTAINER_NAME = os.environ.get(
    'SWIFT_CONTAINER_NAME', 'leonardo')
SWIFT_AUTO_CREATE_CONTAINER = True
SWIFT_AUTO_CREATE_CONTAINER_PUBLIC = True

# ALL MEDIA ARE PUBLIC
MEDIA_ENABLE_PERMISSIONS = False
DEFAULT_MEDIA_STORAGES = {
    'public': {
        'main': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'UPLOAD_TO': 'filer.utils.generate_filename.by_date',
            'OPTIONS': {},
            'UPLOAD_TO_PREFIX': 'uploads',
        },
        'thumbnails': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'OPTIONS': {},
            'THUMBNAIL_OPTIONS': {
                'base_dir': 'public_thumbnails',
            },
        },
    },
    'private': {
        'main': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'OPTIONS': {},
            'UPLOAD_TO': 'filer.utils.generate_filename.by_date',
            'UPLOAD_TO_PREFIX': 'private',
        },
        'thumbnails': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'OPTIONS': {},
            'THUMBNAIL_OPTIONS': {},
        },
    },
}

INTERNAL_IPS = ['*']
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

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
