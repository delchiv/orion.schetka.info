from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'orion_project.views.index', name='index'),

    url(r'^api/auth/', include('rest_auth.urls')),

    url(r'^', include('base.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
