from .base import *


# Database
#ALLOWED_HOSTS = ['vinilwebhn.herokuapp.com']

ALLOWED_HOSTS = ['*']
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


DATABASES = {
    'default': {
        'ENGINE': 'postgresql://${{ PGUSER }}:${{ PGPASSWORD }}@${{ PGHOST }}:${{ PGPORT }}/${{ PGDATABASE }}',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'eLYD592WKJ6qozX1g1s3',
        'HOST': 'containers-us-west-33.railway.app',
        'PORT': '6677',
    }
}



