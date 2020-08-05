import os
from .settings import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

debug_option = os.environ.get('DEBUG').lower()
if debug_option == 'true':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASE_URL = os.environ.get('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_HOST_USER = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True