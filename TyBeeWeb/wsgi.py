"""
WSGI config for TyBeeWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import sys

path = '/srv/www/club/tybee/'
if path not in sys.path:
    sys.path.append(path)

import os

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"]= "TyBeeWeb.settings"

application = get_wsgi_application()
