#!/bin/sh

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput


# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# create superuser
echo "Creating superuser..."
python manage.py createsuperuser --noinput

# Start server using gunicorn
echo "Starting server..."
gunicorn DjangoPost.wsgi --bind=0.0.0.0:80
