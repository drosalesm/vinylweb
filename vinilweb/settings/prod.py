from .base import *
import dj_database_url

# Database
#ALLOWED_HOSTS = ['vinilwebhn.herokuapp.com']
ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://jdmejia:123david@database-1.cqxiuo4vikrc.us-east-1.rds.amazonaws.com:5432/vinylwebhndb",
    )
}




#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'vinylwebhndb',
#        'USER': 'jdmejia',
#        'PASSWORD': '123david',
#        'HOST': 'database-1.cqxiuo4vikrc.us-east-1.rds.amazonaws.com',
#        'PORT': '5432',
#    }
#}



