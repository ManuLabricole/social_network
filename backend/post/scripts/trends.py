import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_project.settings")
django.setup()
