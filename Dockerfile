FROM python:3.8-slim
ARG port

USER root
COPY . /talktohelp
WORKDIR /talktohelp

ENV PORT=$port

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install curl \
    && apt-get install libgomp1

RUN chgrp -R 0 /talktohelp \
    && chmod -R g=u /talktohelp \
    && pip install pip --upgrade 
 
EXPOSE $PORT

CMD gunicorn app:server --bind 0.0.0.0:$PORT --preload