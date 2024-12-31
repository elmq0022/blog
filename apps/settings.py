import os
from pathlib import Path

import dj_database_url


def strtobool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value

    if value.lower() in ["t", "true", "1"]:
        return True

    return False


# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = Path(__file__).resolve().parent
BASE_DIR = PROJECT_DIR.parent
SQLITE_DB = str((BASE_DIR / 'db.sqlite3').absolute())
SITE_ID = 2

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "")
AWS_S3_SIGNATURE_VERSION = os.environ.get("AWS_S3_SIGNATURE_VERSION", "")
AWS_QUERYSTRING_EXPIRE = 604800
USE_CLOUDFRONT = strtobool(os.environ.get("USE_CLOUDFRONT"))
CLOUDFRONT_DOMAIN = os.environ.get("CLOUDFRONT_DOMAIN")

STATIC_LOCATION = "staticfiles"
STATIC_URL = f"{CLOUDFRONT_DOMAIN}/static/" if USE_CLOUDFRONT else "/static/"
MEDIA_URL = f"{CLOUDFRONT_DOMAIN}/media/" if USE_CLOUDFRONT else "/media/"

STORAGES = {
    "staticfiles": {
        "BACKEND": "apps.storages_backends.StaticStorage" \
            if USE_CLOUDFRONT else \
            'django.contrib.staticfiles.storage.StaticFilesStorage',
    },
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(os.environ.get("DEBUG", False))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split("|")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    # Third Party Apps
    "crispy_bootstrap5",
    "crispy_forms",
    'django_recaptcha',
    'tinymce',
    # Project Apps
    'apps.blog',
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

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / "templates", ],
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

WSGI_APPLICATION = 'apps.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# default is for local production provide DATABASE_URL environment variable for production setting
DATABASES = {
    'default': dj_database_url.config(
        default="sqlite:///" + SQLITE_DB
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/
USE_TZ = False
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

###
# CRISPY FORMS
###
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

###
# RECAPTCHA
# default keys are google's test keys
###
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY", None)
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY", None)
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error'] if DEBUG else []

###
# SENDGRID
###
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", None)
TO_EMAIL = os.environ.get("TO_EMAIL", None)
FROM_EMAIL = os.environ.get("FROM_EMAIL", None)

###
# TINYMCE
###
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": True,
    "plugins":
        "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
        "searchreplace,visualblocks,code,codesample,fullscreen,insertdatetime,media,table,paste,"
        "code,help,wordcount",
    "toolbar":
        "undo redo | formatselect | "
        "bold italic backcolor | alignleft aligncenter alignright alignjustify | "
        "image codesample | "
        " bullist numlist outdent indent | "
        "removeformat | help",
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = False
