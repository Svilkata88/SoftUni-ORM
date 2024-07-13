import os
import django

from main_app import apps

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Smartphone

print(apps.get_model('main_app', 'Smartphone'))


