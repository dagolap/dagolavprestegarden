from django.contrib.admin import site

from .models import Project

site.register(Project)