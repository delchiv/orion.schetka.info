# coding: utf-8

from rest_framework import serializers

from .models import Menu, SpTvr, SpGrp


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('num', 'name', 'link', 'level')


class SpTvrSerializer(serializers.ModelSerializer):
#    grp_name = serializers.CharField(source='grp', read_only=True)

    class Meta:
        model = SpTvr
#        fields = ('id', 'num', 'name', 'grp', 'grp_name')
        fields = ('id', 'num', 'name', 'grp',)
        depth = 1

class SpGrpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpGrp
        fields = ('id', 'num', 'name')
