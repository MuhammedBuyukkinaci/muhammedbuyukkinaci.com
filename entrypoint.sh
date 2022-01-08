#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database makemigrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrate"
python manage.py migrate

# Start server
echo "Starting gunicorn server"
gunicorn --bind :8000 --workers 3 personalwebsite.wsgi:application