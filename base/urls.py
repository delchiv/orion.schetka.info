from django.conf.urls import patterns, include, url

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'sptvr', views.SpTvrViewSet)
router.register(r'spgrp', views.SpGrpViewSet)
#router.register(r'doctvr', views.DocTvrViewSet, base_name='doctvr')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),

    url(r'^doctvr(/(?P<pk>\d+))?/$', views.DocTvrViewSet.as_view({'get':'retrive'}), name='doctvr'),
)