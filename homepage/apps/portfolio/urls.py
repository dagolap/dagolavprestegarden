from django.conf.urls import patterns, url

from .views import PortfolioListView, ProjectDetailView

urlpatterns = patterns('',
    url(r'^$', PortfolioListView.as_view(), name="portfolio_index"),
    url(r'^details/(?P<slug>[\w-]+)/$', ProjectDetailView.as_view(), name="project_details"),
)