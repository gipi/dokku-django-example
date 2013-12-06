web: gunicorn dokku_example.wsgi:application
celery: celery worker --beat --app dokku_example --loglevel info
