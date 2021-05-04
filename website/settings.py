"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import json
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.core.management.utils import get_random_secret_key
from dotenv import dotenv_values

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

secret_file = BASE_DIR / ".secrets.json"
if secret_file.exists():
    SECRET_KEY = json.loads(secret_file.read_text())["SECRET_KEY"]
else:
    SECRET_KEY = get_random_secret_key()
    secret_file.write_text(
        json.dumps({"SECRET_KEY": SECRET_KEY}, ensure_ascii=False, indent=2)
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

USE_DEBUG_TOOLBAR = DEBUG

ALLOWED_HOSTS = []


if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]

    ALLOWED_HOSTS = ["localhost", "local.pyyyc.org"]


# Application definition

INSTALLED_APPS = [
    "pyyyc",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *(["debug_toolbar"] if USE_DEBUG_TOOLBAR else []),
]

MIDDLEWARE = [
    *(["debug_toolbar.middleware.DebugToolbarMiddleware"] if USE_DEBUG_TOOLBAR else []),
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "website.wsgi.application"

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_COLLAPSED": True,
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

env_file = dotenv_values(BASE_DIR / ".env")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env_file["MYSQL_DATABASE"],
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": env_file["MYSQL_USER"],
        "PASSWORD": env_file["MYSQL_PASSWORD"],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
