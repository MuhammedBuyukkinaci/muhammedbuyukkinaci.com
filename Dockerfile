FROM python:3.9.9-alpine3.14

# File Author / Maintainer
LABEL maintainer="Muhammed Buyukkinaci @MuhammedBuyukkinaci"

ADD requirements.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps libpq jpeg-dev zlib-dev libjpeg postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD . /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c" , "/app/entrypoint.sh"]
