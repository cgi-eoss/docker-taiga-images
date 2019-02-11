FROM alpine:latest

EXPOSE 8001

RUN apk add --no-cache \
 bash \
 build-base \
 gettext \
 libffi-dev \
 libjpeg-turbo-dev \
 libxml2-dev \
 libxslt-dev \
 postgresql-dev \
 py3-virtualenv \
 python3 \
 python3-dev

# Prepare taiga user and update file ownership
RUN mkdir -p /taiga \
 && adduser -u 1000 -S taiga \
 && chown -R taiga /taiga

# Switch user and prepare taiga-back dependencies
USER taiga

WORKDIR /taiga/taiga-back

COPY taiga-back /taiga/taiga-back

RUN virtualenv /taiga/virtualenv \
 && source /taiga/virtualenv/bin/activate \
 && pip install -r requirements.txt


# Add config and scripts
COPY init.sh /taiga/init.sh
COPY checkdb.py /taiga/checkdb.py
COPY run.sh /taiga/run.sh
COPY docker.py /taiga/taiga-back/settings/docker.py
COPY local.py /taiga/taiga-back/settings/local.py
COPY celery_local.py /taiga/taiga-back/settings/celery_local.py

ENTRYPOINT ["/taiga/run.sh"]
