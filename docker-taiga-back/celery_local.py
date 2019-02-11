from .celery import *
from .docker import *

broker_url = BROKER_URL or None
result_backend = CELERY_RESULT_BACKEND or None
