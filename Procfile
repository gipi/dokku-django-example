web: gunicorn dokku_example.wsgi:application
worker: celery worker --beat --app dokku_example --loglevel info
