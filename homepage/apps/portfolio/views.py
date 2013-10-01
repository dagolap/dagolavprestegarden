from django.views.generic import ListView, DetailView

from .models import Project

class PortfolioListView(ListView):
    template_name = "portfolio/index.html"
    queryset = Project.objects.order_by('-sort_order')

class ProjectDetailView(DetailView):
    template_name="portfolio/project-details.html"
    model=Project