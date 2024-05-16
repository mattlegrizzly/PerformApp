#!/bin/bash

export PGPASSWORD=$DB_PASSWORD
echo "Starting django " 

touch ~/.pgpass
echo $DB_HOST:*:$DB_NAME:$DB_USER:$DB_PASSWORD > ~/.pgpass

# Assuming you're using Postgres, wait for it to start up
until psql -c --no-password -h $DB_HOST -U $DB_USER -d $DB_NAME '\l'; do
  echo "Postgres " $DB_HOST " is unavailable - sleeping" 
  sleep 1
done

echo "Postgres is up - executing command"


echo "Collecting static files..."
python manage.py collectstatic --no-input
echo "Finished collecting static files"

echo "Starting migrations..."
python manage.py makemigrations
python manage.py migrate
echo "Migrations up to date"

echo "Starting Gunicorn server..."
gunicorn backend.wsgi:application --bind $GUNICORN_BIND_HOST:$PORT