from django.conf.urls import patterns, include, url

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'rawm-prihod-doc', views.PrihodDocViewSet)
router.register(r'rawm-prihod-tvr', views.PrihodTvrViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)