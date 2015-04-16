# coding: utf-8

from rest_framework import serializers

from .models import Menu, SpTvr, SpGrp, Doc, Tvr


class MenuSerializer(serializers.ModelSerializer):
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


class DocSerializer(serializers.ModelSerializer):
    org_dt__name = serializers.CharField(source='org_dt.name', read_only=True)
    org_kt__name = serializers.CharField(source='org_kt.name', read_only=True)
    tvr_dt__name = serializers.CharField(source='tvr_dt.name', read_only=True)
    tvr_kt__name = serializers.CharField(source='tvr_kt.name', read_only=True)

    class Meta:
        model = Doc

class TvrSerializer(serializers.ModelSerializer):
    tvr_dt__name = serializers.CharField(source='tvr_dt.name', read_only=True)
    tvr_kt__name = serializers.CharField(source='tvr_kt.name', read_only=True)

    class Meta:
        model = Tvr
