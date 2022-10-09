from .base import *
# Database
DEBUG = True
ALLOWED_HOSTS = ['*']
import dj_database_url

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

#DATABASES = {
  #  'default': {
  #      'ENGINE': 'django.db.backends.postgresql',
 #       'NAME': 'vinylwebhndb',
#        'USER': 'jdmejia',
#        'PASSWORD': '123david',
#        'HOST': 'database-1.cqxiuo4vikrc.us-east-1.rds.amazonaws.com',
#        'PORT': '5432',
#    }
#}



DATABASES = {
    "default": dj_database_url.config(
        default="postgres://cshhdkvvrbtwjh:d61b4cd114ea3284ddc40f5cc6f765b57295ae4988a060a7083d58a94f9e0028@ec2-44-198-82-71.compute-1.amazonaws.com:5432/dcehk2opl42hop",
    )
}