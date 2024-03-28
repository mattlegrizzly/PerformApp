#!/bin/bash

export PGPASSWORD=$DB_PASSWORD

until psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c '\l'; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - executing command"
touch ~/.pgpass
echo $DB_HOST:*:$DB_NAME:$DB_USER:$DB_PASSWORD > ~/.pgpass

echo "Starting migrations..."
python manage.py migrate

# echo "Starting server..."

# python manage.py runserver 0.0.0.0:8000