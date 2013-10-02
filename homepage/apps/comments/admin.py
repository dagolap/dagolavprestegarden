from django.contrib.admin import site

from .models import Comment

site.register(Comment)