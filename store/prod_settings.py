import os
from .settings import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASE_URL = os.environ.get('DATABASE_URL')

DATABASE = {
    'default': dj_database_url.config(os.environ.get('DATABASE_URL'))
}