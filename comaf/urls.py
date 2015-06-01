from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comaf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.base.urls')),
    url(r'^metric/', include('apps.metrics.urls')),
    # REST Api urls
    url(r'^api/', include('apps.api.urls')),

)
