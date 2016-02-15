from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'logging_fun.views.home', name='home'),
    url(r'^buggy/?$', 'logging_fun.views.buggy', name='home_debug'),
    url(r'^500/?$', 'logging_fun.views.raise_500', ),
    url(r'^delay/?$', 'logging_fun.views.delay', ),
    url(r'^db/?$', 'logging_fun.views.hit_db', ),
    url(r'^springboard/?$', 'logging_fun.views.springboard', ),
    url(r'^unconfigured/', include('unconfigured.urls', namespace='unconfigured')),
)
