from django.conf.urls import patterns, url

from .views import BlogListView, PostDetailView

urlpatterns = patterns('',
    url(r'^$', BlogListView.as_view(), name="blog_index"),
    url(r'^details/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name="post_details"),
)