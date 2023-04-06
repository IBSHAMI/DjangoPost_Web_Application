#!/bin/sh

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Make database migrations
echo "Making database migrations..."
python manage.py makemigrations

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Load data from the fixture file
echo "Loading data from the fixture file..."
python manage.py loaddata data.json

# Create superuser
echo "Creating superuser..."
python manage.py createsuperuser --noinput

# Start server using gunicorn
echo "Starting server..."
gunicorn DjangoPost.wsgi --bind=0.0.0.0:80
