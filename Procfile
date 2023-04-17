release: python manage.py makemigrations && python manage.py migrate
web: gunicorn egz.wsgi:application
