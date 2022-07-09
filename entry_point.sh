sleep 1 # experimental, let other services be READY to listen on ports :)
python manage.py migrate
python manage.py init_admin
gunicorn --bind unix:/socket/gunicron.sock --bind 0.0.0.0:8000 -w 2 escrow.wsgi  --access-logfile /logs/gunicron_access.log --error-logfile /logs/gunicron_error.log
