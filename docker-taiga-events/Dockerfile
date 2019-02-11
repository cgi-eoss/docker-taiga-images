FROM alpine:latest

EXPOSE 8888

RUN apk add --no-cache \
 nodejs \
 npm

COPY taiga-events /taiga/taiga-events

WORKDIR /taiga/taiga-events

RUN mkdir -p /taiga \
 && adduser -u 1000 -S taiga \
 && chown -R taiga /taiga

USER taiga

RUN npm install --production \
 && npm install coffeescript

ENTRYPOINT ["node_modules/coffeescript/bin/coffee", "index.coffee"]