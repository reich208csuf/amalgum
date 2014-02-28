"""
WSGI config for webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
#might need to delete next line...
sys.path.append('/srv/csci152proj/app/webapp/webapp/')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
