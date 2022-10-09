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
        default="postgres://david:ZDHyVTIfvwsbtPDQvf68569WNIHNClip@dpg-ccvra3da4994l0ckk77g-a/restdjangodb",                 
    )
}



#DATABASES = {
#    "default": dj_database_url.config(
#        default="postgres://jdmejia:123david@database-1.cqxiuo4vikrc.us-east-1.rds.amazonaws.com:5432/vinylwebhndb",
#    )
#}
