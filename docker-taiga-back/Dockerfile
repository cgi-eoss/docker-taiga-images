FROM python:3.6-alpine

EXPOSE 8001

RUN apk add --no-cache \
 bash \
 build-base \
 gettext \
 libffi-dev \
 libjpeg-turbo-dev \
 libxml2-dev \
 libxslt-dev \
 postgresql-dev
RUN pip install virtualenv

WORKDIR /taiga/taiga-back

COPY taiga-back /taiga/taiga-back

# Add config and scripts
COPY init.sh /taiga/init.sh
COPY checkdb.py /taiga/checkdb.py
COPY run.sh /taiga/run.sh
COPY docker.py /taiga/taiga-back/settings/docker.py
COPY local.py /taiga/taiga-back/settings/local.py
COPY celery_local.py /taiga/taiga-back/settings/celery_local.py

# Prepare taiga user and update file ownership
RUN mkdir -p /taiga \
 && adduser -u 1000 -S taiga \
 && chown -R taiga /taiga

# Switch user and prepare taiga-back dependencies
USER taiga

RUN virtualenv --python=python3.6 /taiga/virtualenv \
 && source /taiga/virtualenv/bin/activate \
 && pip install -r requirements.txt

ENTRYPOINT ["/taiga/run.sh"]
