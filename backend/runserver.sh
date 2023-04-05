#!/bin/sh

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# create superuser
python manage.py createsuperuser --noinput

# Start server using gunicorn
gunicorn DjangoPost.wsgi --bind=0.0.0.0:80
