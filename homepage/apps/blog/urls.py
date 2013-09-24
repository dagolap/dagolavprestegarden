from django.conf.urls import patterns, url

from django.views.generic import DetailView, ListView

from .views import BlogListView, PostDetailView
from .models import Post

urlpatterns = patterns('',
    url(r'^$', BlogListView.as_view(), name="blog_index"),
    url(r'^details/(?P<slug>\w+)/$', PostDetailView.as_view(), name="post_details"),
)