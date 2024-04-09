"""
Django settings for ccresponse project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

from environ import Env

env = Env()

env.read_env(env_file='.env')
env.read_env(env_file='config/.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env('DJANGO_DEBUG', default=False)

# ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=[])
# ALLOWED_HOSTS = ['.ngrok-free.app','localhost','127.0.0.1']
ALLOWED_HOST = ['*']
# Application definition

SHARED_APPS = [
    'django_tenants',
    'client',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
    'django_filters',

    'corsheaders',
    'drf_yasg',
    'rest_framework_simplejwt.token_blacklist',
    'huey.contrib.djhuey',

    'core',
    'parties',
    'vehicles',
    'cases',
    'common',
    'api',
    'documents',
    'notification',
    'chat',
    'invoices',
    'reports',
]

TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
    'django_filters',

    'corsheaders',
    'drf_yasg',
    'rest_framework_simplejwt.token_blacklist',
    'huey.contrib.djhuey',

    'core',
    'parties',
    'vehicles',
    'cases',
    'common',
    'api',
    'documents',
    'notification',
    'chat',
    'invoices',
    'reports',
]

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = 'client.Client'
TENANT_DOMAIN_MODEL = 'client.Domain'

SHOW_PUBLIC_IF_NO_TENANT_FOUND = True

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEFAULT_DATE_FORMAT = '%d/%m/%Y'
DEFAULT_TIME_FORMAT = '%H:%M:%S'
DEFAULT_DATETIME_FORMAT = f'{DEFAULT_DATE_FORMAT} {DEFAULT_TIME_FORMAT}'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'TIME_FORMAT': DEFAULT_TIME_FORMAT,
    'TIME_INPUT_FORMATS': [DEFAULT_TIME_FORMAT],
    'DATE_FORMAT': DEFAULT_DATE_FORMAT,
    'DATE_INPUT_FORMATS': [DEFAULT_DATE_FORMAT],
    'DATETIME_FORMAT': DEFAULT_DATETIME_FORMAT,
    'DATETIME_INPUT_FORMATS': [DEFAULT_DATETIME_FORMAT]
}

PUBLIC_SCHEMA_URLCONF = 'ccresponse.urls'
ROOT_URLCONF = 'ccresponse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ccresponse.wsgi.application'
ASGI_APPLICATION = 'ccresponse.routing.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
import dj_database_url

DB = env.db()
DB['ENGINE'] = 'django_tenants.postgresql_backend'

DATABASES = {
    'default': dj_database_url.config(default=env('DATABASE_URL'))
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

AUTHENTICATION_BACKENDS = ['core.backends.EmailBasedAuthenticationBackend']

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

ATOMIC_REQUESTS = True

AUTH_USER_MODEL = 'core.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    # Create task to flushexpiredtokens every n days:
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/blacklist_app.html
    'ROTATE_REFRESH_TOKENS': True,
    # 'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
}

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
S3_WORKING_FOLDER = env('S3_WORKING_FOLDER')
AWS_S3_SIGNATURE_VERSION = "s3v4"

MEDIA_URL = '/media/'
AWS_PUBLIC_MEDIA_LOCATION = f'{S3_WORKING_FOLDER}{MEDIA_URL}public'
DEFAULT_FILE_STORAGE = 'ccresponse.storage_backends.PublicMediaStorage'

AWS_PRIVATE_MEDIA_LOCATION = f'{S3_WORKING_FOLDER}{MEDIA_URL}private'
PRIVATE_FILE_STORAGE = 'ccresponse.storage_backends.PrivateMediaStorage'

FRONTEND_URL = env('FRONTEND_URL')
FRONTEND_FORGOT_PASSWORD_PATH = env('FRONTEND_FORGOT_PASSWORD_PATH')
FRONTEND_EMAIL_VERIFY_PATH = env('FRONTEND_EMAIL_VERIFY_PATH')
FRONTEND_REGISTRATION_VERIFY_PATH = env('FRONTEND_REGISTRATION_VERIFY_PATH')
CORS_ALLOWED_ORIGINS = ['https://6178-103-120-70-154.ngrok-free.app','http://localhost:3000','https://ccresponse-backend.up.railway.app']
# CORS_ALLOWED_ORIGIN_REGEXES = [env('CORS_ALLOWED_ORIGIN_REGEXES')]
HOSTS_ALLOWED_TO_RESET_PASSWORD = [FRONTEND_URL]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

REPORT_EMAIL_HOST = env('REPORT_EMAIL_HOST')
REPORT_EMAIL_HOST_USER = env('REPORT_EMAIL_HOST_USER')
REPORT_EMAIL_HOST_PASSWORD = env('REPORT_EMAIL_HOST_PASSWORD')
REPORT_EMAIL_PORT = env('REPORT_EMAIL_PORT')
REPORT_EMAIL_USE_TLS = env('REPORT_EMAIL_USE_TLS')
REPORT_DEFAULT_FROM_EMAIL = env('REPORT_DEFAULT_FROM_EMAIL')

TWILIO_ACCOUNT_SID = env('TWILIO_ACCOUNT_SID')
TWILIO_ACCOUNT_AUTH_TOKEN = env('TWILIO_ACCOUNT_AUTH_TOKEN')
TWILIO_ACCOUNT_SENDER_NUMBER = env('TWILIO_ACCOUNT_SENDER_NUMBER')

DOCUSIGN_USERNAME = env('DOCUSIGN_USERNAME')
DOCUSIGN_PASSWORD = env('DOCUSIGN_PASSWORD')
DOCUSIGN_USER_ID = env('DOCUSIGN_USER_ID')
DOCUSIGN_CLIENT_ID = env('DOCUSIGN_CLIENT_ID')
DOCUSIGN_ACCOUNT_ID = env('DOCUSIGN_ACCOUNT_ID')
DOCUSIGN_BASE_PATH = env('DOCUSIGN_BASE_PATH')
DOCUSIGN_AUTH_SERVER = env('DOCUSIGN_AUTH_SERVER')
DOCUSIGN_PRIVATE_KEY = env('DOCUSIGN_PRIVATE_KEY')

# Default = 12 hours
PASSWORD_RESET_TIMEOUT = env('PASSWORD_RESET_TIMEOUT', default=12 * 60 * 60)

CASES_DEFAULT_PAGE_SIZE = 50
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

HUEY = {
    'huey_class': 'huey.RedisHuey',  # Huey implementation to use.
    'immediate': False,
    'connection': {
        'host': 'redis',
        'port': 6379,
        'db': 0,
        'connection_pool': None,  # Definitely you should use pooling!

        'read_timeout': 1,  # If not polling (blocking pop), use timeout.
        'url': None,  # Allow Redis config via a DSN.
    },
    'consumer': {
        'workers': 4,
        'worker_type': 'thread',
        'initial_delay': 0.1,  # Smallest polling interval, same as -d.
        'backoff': 1.15,  # Exponential backoff using this rate, -b.
        'max_delay': 10.0,  # Max possible polling interval, -m.
        'scheduler_interval': 1,  # Check schedule every second, -s.
        'periodic': True,  # Enable crontab feature.
        'check_worker_health': True,  # Enable worker health checks.
        'health_check_interval': 1,  # Check worker health every second.
    },
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')