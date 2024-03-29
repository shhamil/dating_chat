#! /bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

echo "from dating_chat.models import Client; Client.objects.create_superuser(username='admin', email='admin@example.com', password='admin')" | python manage.py shell
exec gunicorn config.wsgi:application -b 0.0.0.0:80 --reload