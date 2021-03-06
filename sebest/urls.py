from django.conf.urls import patterns, include, url

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sebest', views.SebestViewSet, base_name='sebest')
router.register(r'cena', views.CenaDocViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)