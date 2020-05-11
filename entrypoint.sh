#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

cd /src
python manage.py migrate --noinput
echo "migrate complete..."

service cron start
python manage.py crontab add
python manage.py crontab add

python manage.py collectstatic --noinput
echo "collectstatic complete..."

gunicorn social_auth_mymapa.wsgi:application -w 3 -b 0.0.0.0:8001

exec "$@"