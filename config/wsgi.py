"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")

sys.path.append(os.environ["VIRTUAL_ENV"] + "/Lib/site-packages")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
