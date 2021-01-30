#!/bin/bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn --bind ":80" --worker-class=gevent --worker-connections=1000  --workers 6 "vocab_django.wsgi:application"