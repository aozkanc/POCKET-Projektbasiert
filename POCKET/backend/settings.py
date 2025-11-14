import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC FILE SETTINGS
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # Directory containing static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory where static files collected by Django are saved


SECRET_KEY = 'django-insecure-sy)$lg)q)s71#(-!me*f25(u-e-8yqmsl=i!a1d(lcjp0(3rkq'

DEBUG = True  # for Testing True, make it false in Production

ALLOWED_HOSTS = ["*"]  # open for Docker

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'core',  # Main application
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'core.validators.CustomPasswordValidator',  # Use special password validator only
    },
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # for error message
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # for error message
    'django.contrib.messages.middleware.MessageMiddleware',  # for error message
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# **TEMPLATE SETTINGS**
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Updated!
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

# **DATABASE (MySQL)**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pocket_db',
        'USER': 'pocket_user',
        'PASSWORD': 'pocket_password',
        'HOST': 'db',
        'PORT': '3306',
    }
}

# **OTHER SETTINGS**
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'  # Germany time zone
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

ROOT_URLCONF = 'backend.urls'  # If backend file contains the main urls

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

