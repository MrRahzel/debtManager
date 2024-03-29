"""
Django settings for debtManager project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0n=zsc005_rq2)$f!&jca7ie8$a%*(9&+20%vmbf3g3q4n_*aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['timebank72.ru', 'www.timebank72.ru', 'localhost']
#CSRF_TRUSTED_ORIGINS = ['https://timebank72.ru']


#AUTH_USER_MODEL = 'debtManager.Usvers'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   #'accounts',
    'accounts.apps.AccountsConfig',
    'django_cleanup',
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

ROOT_URLCONF = 'debtManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'accounts/Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#TEMPLATE_DIRS = [
#    os.path.join(SETTINGS_PATH, 'templates'),
#]


WSGI_APPLICATION = 'debtManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'DISABLE_SERVER_SIDE_CURSORS': True,
        'PASSWORD': 'aaa',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#STATIC_DIR = os.path.join(BASE_DIR, '/home/user1/var/www/timebank72/debtManager/accounts/static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, '/var/www/timebank72.ru/debtManager/accounts/static/')]
STATIC_URL = '/debtManager/accounts/static/'
#STATIC_URL = 'static'
STATIC_ROOT= os.path.join(BASE_DIR, "/var/www/timebank72.ru/static/")
#MEDIA_URL = '/debtManager/accounts/media/'
MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'accounts/media')
#STATIC_ROOT= os.path.join(BASE_DIR, "/var/www/timebank72.ru/debtManager/accounts/static/")
#MEDIA_URL = '/media/'
#MEDIA_ROOT = '/var/www/timebank72.ru/debtManager/accounts/static/images'

LOGIN_URL='/profile/index'
LOGIN_REDIRECT_URL = '/profile'
LOGOUT_REDIRECT_URL = '/login'

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
                },
            },

}
"""
