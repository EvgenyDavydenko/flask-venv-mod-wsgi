import sys
sys.path.insert(0, '/var/www/flask/flask-venv-mod-wsgi')
sys.path.insert(1, '/var/www/flask/flask-venv-mod-wsgi/venv/lib/python3.8/site-packages')

from flaskapp import app as application
