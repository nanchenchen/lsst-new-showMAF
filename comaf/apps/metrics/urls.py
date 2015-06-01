from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

import comaf.apps.metrics.views as views

urlpatterns = patterns('comaf.apps.metrics.views',

                     # All project-related-urls should start with the project code: ^(?P<project_pk>\d+)/
                       url(r'^(?P<pk>\d+)/$',
                           views.MetricDetailView.as_view(),
                           name='metric'),

)
