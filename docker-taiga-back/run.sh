#!/bin/bash

set -x

TAIGA_BACK_ROOT="/taiga/taiga-back"

cd ${TAIGA_BACK_ROOT} && source /taiga/virtualenv/bin/activate

# Last-minute migrations in case we are upgrading an installed site
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py compilemessages

gunicorn -w3 -t60 --pythonpath=. -b 0.0.0.0:8001 taiga.wsgi
