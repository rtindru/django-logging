from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'unconfigured.views.home', name='unconfigured_home'),
)
