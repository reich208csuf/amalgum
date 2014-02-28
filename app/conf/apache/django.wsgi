#http://www.lennu.net/2012/05/14/django-deployement-installation-to-ubuntu-12-dot-04-server/
#read this page^ 
#it walks you through serving django via apache2 
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'venv/lib/python2.7/site-packages/')))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'app')))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'app', 'webapp')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'webapp.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
