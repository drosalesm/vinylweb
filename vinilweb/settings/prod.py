from .base import *
import dj_database_url

# Database
#ALLOWED_HOSTS = ['vinilwebhn.herokuapp.com']
ALLOWED_HOSTS = ['*']

#DATABASES = {
#    "default": dj_database_url.config(
#        default="postgres://jdmejia:123david@database-1.cqxiuo4vikrc.us-east-1.rds.amazonaws.com:5432/vinylwebhndb",
#    )
#}

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://cshhdkvvrbtwjh:d61b4cd114ea3284ddc40f5cc6f765b57295ae4988a060a7083d58a94f9e0028@ec2-44-198-82-71.compute-1.amazonaws.com:5432/dcehk2opl42hop",
    )
}


#ALLOWED_HOSTS = ['*']
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'da435ej10i352j',
#        'USER': 'lkuvnmjabcrixk',
#        'PASSWORD': '15683ab85c93f7c61aba3180f79f24e94d49fb0a22f7fb23e6d073b010227838',
#        'HOST': 'ec2-52-20-166-21.compute-1.amazonaws.com',
#        'PORT': '5432',
#    }
#}


