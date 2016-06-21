"""
WSGI config for fromleaf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys

from django.core.wsgi import get_wsgi_application

if "APP_IS_ON_AWS" in os.environ:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fromleaf.settings.aws_settings")
elif "APP_IS_ON_AZURE" in os.environ:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fromleaf.settings.azure_settings")
else:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fromleaf.settings.settings")


try:
	application = get_wsgi_application()
except Exception:
	if 'mod_wsgi' in sys.modules:
		traceback.print_exc()
		os.kill(os.getpid(), signal.SIGINT)
		time.sleep(2.5)