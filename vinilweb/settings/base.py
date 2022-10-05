
from pathlib import Path

import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)
from django.urls import reverse_lazy


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oq)#zxs4mc$$6ky455_k9&@0i9+q&@s5pn%8546e@q@n9=#__p'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'widget_tweaks',
    'applications.landing',
    'django.contrib.humanize',
    'embed_video'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'vinilweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
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

WSGI_APPLICATION = 'vinilweb.wsgi.application'





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



STATIC_URL = '/static/' 
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'

#Configurar la ruta static



STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')   #este es el original
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')   #este es el nuevo
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
STATIC_TMP = os.path.join(BASE_DIR, 'static')

django_heroku.settings(locals())

#AUTH_USER_MODEL = 'usuarios_inova.User'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
