from django.views.generic import DetailView

from .models import Page

class PageDetailView(DetailView):
    template_name="pages/page.html"
    model=Page