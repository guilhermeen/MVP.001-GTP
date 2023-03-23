# ecommerce/__init__.py

import os
import sys

# Add the apps directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "apps"))

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")

# Load the application instance
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()