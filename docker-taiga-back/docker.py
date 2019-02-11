# Importing common provides default settings, see:
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TAIGA_DB_NAME'),
        'HOST': os.getenv('TAIGA_DB_HOST'),
        'USER': os.getenv('TAIGA_DB_USER'),
        'PASSWORD': os.getenv('TAIGA_DB_PASSWORD')
    }
}

TAIGA_PROTOCOL = os.getenv('TAIGA_PROTOCOL')
TAIGA_HOSTNAME = os.getenv('TAIGA_HOSTNAME')

SITES['api']['domain'] = TAIGA_HOSTNAME
SITES['front']['domain'] = TAIGA_HOSTNAME

MEDIA_URL  = "%s://%s/media/" % (TAIGA_PROTOCOL, TAIGA_HOSTNAME)
STATIC_URL = "%s://%s/static/" % (TAIGA_PROTOCOL, TAIGA_HOSTNAME)

SECRET_KEY = os.getenv('TAIGA_SECRET_KEY')

if os.getenv('TAIGA_RABBIT_URL') is not None and os.getenv('TAIGA_REDIS_URL') is not None:
    from .celery import *

    BROKER_URL = os.getenv('TAIGA_RABBIT_URL')
    CELERY_RESULT_BACKEND = os.getenv('TAIGA_REDIS_URL')
    CELERY_ENABLED = True

    EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
    EVENTS_PUSH_BACKEND_OPTIONS = {"url": BROKER_URL}

if os.getenv('TAIGA_ENABLE_EMAIL').lower() == 'true':
    DEFAULT_FROM_EMAIL = os.getenv('TAIGA_EMAIL_FROM')
    CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 # in seconds

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    if os.getenv('TAIGA_EMAIL_USE_TLS').lower() == 'true':
        EMAIL_USE_TLS = True
    else:
        EMAIL_USE_TLS = False

    EMAIL_HOST = os.getenv('TAIGA_EMAIL_HOST')
    EMAIL_PORT = int(os.getenv('TAIGA_EMAIL_PORT'))
    EMAIL_HOST_USER = os.getenv('TAIGA_EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.getenv('TAIGA_EMAIL_PASS')
