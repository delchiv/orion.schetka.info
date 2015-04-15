from django.conf.urls import patterns, include, url

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'components', views.ComponentViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)