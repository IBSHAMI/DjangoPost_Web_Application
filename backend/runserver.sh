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

# create superuser
echo "Creating superuser..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='$DJANGO_SUPERUSER_USERNAME', email='$DJANGO_SUPERUSER_EMAIL', password='$DJANGO_SUPERUSER_PASSWORD')"


# Start server using gunicorn
echo "Starting server..."
gunicorn DjangoPost.wsgi --bind=0.0.0.0:80
