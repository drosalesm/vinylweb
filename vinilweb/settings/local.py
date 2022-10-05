from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

cALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'vinyl_page',
#        'USER': 'postgres',
#        'PASSWORD': '123',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'da435ej10i352j',
        'USER': 'lkuvnmjabcrixk',
        'PASSWORD': '15683ab85c93f7c61aba3180f79f24e94d49fb0a22f7fb23e6d073b010227838',
        'HOST': 'ec2-52-20-166-21.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
