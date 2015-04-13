from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index', name='index'),
)