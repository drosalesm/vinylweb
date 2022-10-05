from .base import *
# Database
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vinyl_page',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


#DATABASES = {  
#    'default': {  
#        'ENGINE': 'django.db.backends.mysql',  
#        'NAME': 'vinyl_page',  
#        'USER': 'root',  
#        'PASSWORD': 'your_password',  
#        'HOST': 'localhost',  
#        'PORT': '5432',  
#    }  
#}  