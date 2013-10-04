from django.conf.urls import patterns, url

from .views import BlogListView, PostDetailView
from .syndication import LatestPostsFeed

urlpatterns = patterns('',
    url(r'^$', BlogListView.as_view(), name="blog_index"),
    url(r'^details/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name="post_details"),
    url(r'^feeds/latest/$', LatestPostsFeed()),
)