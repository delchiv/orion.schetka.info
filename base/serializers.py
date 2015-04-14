# coding: utf-8

from rest_framework import serializers

from .models import Menu, SpTvr

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('num', 'name', 'link', 'level')

class SpTvrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpTvr
        fields = ('id', 'num', 'name')
