#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgresSQL started"
fi

python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py migrate
python manage.py populate_data
python manage.py collectstatic  --no-input
python manage.py test


exec "$@"