"""
Django settings for webserver project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import json
from .secrets import get_secret


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
ALLOWED_HOSTS = ['.facebook.com', '.isptoolbox.io', '.fbctower.com']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if "DEBUG" in os.environ and os.environ.get("DEBUG").lower() == 'true':
    DEBUG = True
    ALLOWED_HOSTS = ['*']

PROD = False
if "PROD" in os.environ and os.environ.get("PROD").lower() != 'false':
    PROD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # Static Files S3
    AWS_DEFAULT_ACL = None

    AWS_STORAGE_BUCKET_NAME = 'isptoolbox-static'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = 'static'
    AWS_CLOUDFRONT_DOMAIN = 'static.isptoolbox.io'
    AWS_S3_CUSTOM_DOMAIN = AWS_CLOUDFRONT_DOMAIN
    STATICFILES_STORAGE = 'isptoolbox_storage.storage.S3ManifestStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'


# Application definition
INSTALLED_APPS = [
    # Async / Websockets
    'channels',
    # IspToolbox User Accounts
    'IspToolboxAccounts',
    # ISP Toolbox App
    'IspToolboxApp',
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'corsheaders',
    # Django Admin Docs
    'django.contrib.admindocs',
    # Other ISP Toolbox Apps
    'mmwave',
    'Overlay',
    'NetworkComparison',
    'dataUpdate',
    'isptoolbox_storage',
    'workspace',
    'gis_data',
    # S3 Static File Storage
    'storages',
    # Social Auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    # REST API
    'rest_framework',
    'django.contrib.humanize',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_collect')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/potree/build/'),
    os.path.join(BASE_DIR, 'static/potree/libs/'),
    os.path.join(BASE_DIR, 'static/isptoolbox/build/')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

WAGTAIL_SITE_NAME = 'Help Center'

CSP_EXCLUDE_URL_PREFIXES = ('cms/', 'pages/',)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

SITE_ID = 1
if PROD:
    SITE_ID = 3

AUTHENTICATION_BACKENDS = (
    'IspToolboxAccounts.backends.EmailBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = "/pro"
ACCOUNT_LOGOUT_REDIRECT_URL = "/pro"
LOGIN_URL = "/pro"

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"

# facebook
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'js_sdk',
        'SDK_URL': '//connect.facebook.net/en_US/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name',
            'email',
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v10.0',
    }
}

ENABLE_ACCOUNT_CREATION = False

# These keys have full access to AWS S3 and secrets manager

FB_SDK_SECRETS = json.loads(get_secret("prod/fb_sdk_isptoolbox",
                                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY))
SOCIAL_AUTH_FACEBOOK_KEY = FB_SDK_SECRETS['fb_sdk_isptoolbox_app_key']  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = FB_SDK_SECRETS['fb_sdk_isptoolbox_app_secret']  # app key
ASN_CURL_SECRET = FB_SDK_SECRETS['asn_fb_curl']

MAPBOX_ACCESS_TOKEN_PUBLIC = 'pk.eyJ1IjoiaXNwdG9vbGJveCIsImEiOiJja2p5eHd1aGcwMjhoMm5wcGkxdnl4N2htIn0.cLO8vp0k2kXclp4CNzwWhQ'
MAPBOX_ACCOUNT = 'isptoolbox'

MAPBOX_SECRETS = json.loads(get_secret("prod/mapbox",
                                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY))
MAPBOX_ACCESS_TOKEN_BACKEND = MAPBOX_SECRETS['MAPBOX_ACCESS_TOKEN_BACKEND']
MAPBOX_ACCOUNT_PASSWORD = MAPBOX_SECRETS['MAPBOX_ACCOUNT_PASSWORD']
MAPBOX_ACCOUNT_EMAIL = MAPBOX_SECRETS['MAPBOX_ACCOUNT_EMAIL']

MAPBOX_PUBLIC_TOKEN = MAPBOX_SECRETS['MAPBOX_PUBLIC_ACCESS_TOKEN_ALLOW_ALL_URL']
if PROD:
    MAPBOX_PUBLIC_TOKEN = MAPBOX_SECRETS['MAPBOX_PUBLIC_ACCESS_TOKEN_FB_ISPTOOLBOX_URL']
TILESET_SECRETS = json.loads(get_secret("prod/tileset_jwt_secret",
                                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY))
TILESET_LAMBDA_EDGE_SECRET = TILESET_SECRETS['TILESET_LAMBDA_EDGE_SECRET']

# This UID and key are used for the cloudrf API, currently using the 10,000 requests/month plan
CLOUD_RF = json.loads(get_secret("prod/cloudrf",
                                 aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY))

CLOUDRF_UID = CLOUD_RF['cloud_rf_uid']
CLOUDRF_KEY = CLOUD_RF['cloud_rf_key']

# This is a tiny, tiny elastic search cluster
ELASTICSEARCH_SECRETS = json.loads(get_secret(
                                    "prod/elastic_search_asn",
                                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY))

ES_ENDPOINT = ELASTICSEARCH_SECRETS['ENDPOINT_ELASTICSEARCH']
USERNAME_ES = ELASTICSEARCH_SECRETS['ADMIN_ELASTICSEARCH']
PASSWORD_ES = ELASTICSEARCH_SECRETS['PASSWORD_ELASTICSEARCH']

MIDDLEWARE = [
    'IspToolboxApp.middleware.HealthCheckMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSP_INCLUDE_NONCE_IN = [
    'default-src',
    'script-src',
    'style-src',
]

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://(.+\.)?facebook\.com$",
]

ROOT_URLCONF = 'webserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'webserver.wsgi.application'
# Channels
ASGI_APPLICATION = 'webserver.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [os.environ.get('REDIS_BACKEND', 'redis://localhost:6379')],
        },
    },
}

# Load Secrets
GIS_DB_CREDENTIALS = json.loads(get_secret("prod/gis_db",
                                           aws_access_key_id=AWS_ACCESS_KEY_ID,
                                           aws_secret_access_key=AWS_SECRET_ACCESS_KEY))
if PROD:
    DJANGO_ORM_DB_CREDENTIALS = json.loads(get_secret("prod/isptoolbox_django",
                                                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                                                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY))
    DJANGO_ORM_DB_CREDENTIALS.update({
        'name': 'django_db',
        'host-read-replica': 'isptoolbox-db-prod-read-replica1.cahmkzzberpf.us-west-1.rds.amazonaws.com',
    })
else:
    DJANGO_ORM_DB_CREDENTIALS = {
        'name': os.environ.get('DB_NAME', 'django_test'),
        'username': os.environ.get('DB_USERNAME', 'postgres'),
        'password': os.environ.get('DB_PASSWORD', 'password'),
        'host': os.environ.get('POSTGRES_DB', 'localhost'),
        'host-read-replica': os.environ.get('POSTGRES_DB', 'localhost'),
        'port': '5432',
    }

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': DJANGO_ORM_DB_CREDENTIALS['name'],
        'USER': DJANGO_ORM_DB_CREDENTIALS['username'],
        'PASSWORD': DJANGO_ORM_DB_CREDENTIALS['password'],
        'HOST': DJANGO_ORM_DB_CREDENTIALS['host'],
        'TEST': {
            'NAME': 'testing_database_isptoolbox',
        },
        'PORT': DJANGO_ORM_DB_CREDENTIALS['port'],
    },
    'default-read-replica': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': DJANGO_ORM_DB_CREDENTIALS['name'],
        'USER': DJANGO_ORM_DB_CREDENTIALS['username'],
        'PASSWORD': DJANGO_ORM_DB_CREDENTIALS['password'],
        'HOST': DJANGO_ORM_DB_CREDENTIALS['host-read-replica'],
        'PORT': DJANGO_ORM_DB_CREDENTIALS['port'],
    },
    # This DB is not managed by Django ORM, therefore we hardcode parameters
    # Contains static GIS data: microsoft buildings dataset, income data, fcc broadband availablility
    'gis_data': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': GIS_DB_CREDENTIALS['username'],
        'PASSWORD': GIS_DB_CREDENTIALS['password'],
        'HOST': GIS_DB_CREDENTIALS['host'],
        'PORT': GIS_DB_CREDENTIALS['port'],
    },
    'gis_data_read_replica': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': GIS_DB_CREDENTIALS['username'],
        'PASSWORD': GIS_DB_CREDENTIALS['password'],
        'HOST': 'isptoolbox-gis-db-prod-read-replica.cahmkzzberpf.us-west-1.rds.amazonaws.com',
        'PORT': GIS_DB_CREDENTIALS['port'],
    }
}

DATABASE_ROUTERS = ['gis_data.models.GISDataRouter']
AUTH_USER_MODEL = "IspToolboxAccounts.User"


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


CELERY_BROKER_URL = os.environ.get('REDIS_BACKEND', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_BACKEND', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Los_Angeles'
