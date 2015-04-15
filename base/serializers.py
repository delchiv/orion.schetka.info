# coding: utf-8

from rest_framework import serializers

from .models import Menu, SpTvr, SpGrp


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu


class SpTvrSerializer(serializers.ModelSerializer):
    grp__name = serializers.CharField(source='grp.name', read_only=True)
    subgrp__name = serializers.CharField(source='subgrp.name', read_only=True)

    class Meta:
        model = SpTvr


class SpGrpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpGrp
