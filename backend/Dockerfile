FROM python:3.11.1-alpine3.17

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY ./requirements.txt /tmp/requirements.txt

COPY . /backend

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user

EXPOSE 8000
