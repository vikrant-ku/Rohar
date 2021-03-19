from .base import *

SECRET_KEY = '#xei5scqncob+pz&1scmif$x(3f$b+n6vm-vi@&vh*xc*3loxz'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','3.6.238.39']




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vikrant.rohartech@gmail.com'
EMAIL_HOST_PASSWORD = 'mezjxzfwrlshlwkb'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}