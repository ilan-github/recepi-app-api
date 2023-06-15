FROM python:3.9-alpine3.17
LABEL maintainer="ilanshe"

ENV PYTHONNUMBUFFERED 1

COPY ./requirments.txt /tmp/requirments.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --uprade pip && \
    /py/bin/pip install -r /tmp/requirments && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user 

ENV PATH="/py/bin:$PATH"

USER django-user
