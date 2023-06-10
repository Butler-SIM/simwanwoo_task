#!/bin/sh

echo "update 2023-06-10 0001"

# Migrate
python manage.py makemigrations
#python manage.py migrate

# Static Files
# python manage.py collectstatic --noinput --settings=config.settings

exec "$@"