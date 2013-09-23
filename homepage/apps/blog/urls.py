from django.conf.urls import patterns, url

from django.views.generic import TemplateView


urlpatterns = patterns('apps.blog',
    url(r'^$', TemplateView.as_view(template_name="blog/index.html")),
)