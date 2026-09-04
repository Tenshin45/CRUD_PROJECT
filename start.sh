set -e

cd PROJECT
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || true
python manage.py collectstatic --noinput
exec gunicorn PROJECT.wsgi --bind 0.0.0.0:${PORT:-8000}