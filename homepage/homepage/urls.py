from django.conf.urls import patterns, include, url
from django.contrib import admin

from filebrowser.sites import site as fbsite

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.blog.views.index', name="index"),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^projects/', include('apps.portfolio.urls')),


    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(fbsite.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
