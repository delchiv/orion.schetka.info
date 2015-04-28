# coding: utf-8

from rest_framework import serializers

from base.serializers import DocSerializer, TvrSerializer

from .models import PrihodDoc, PrihodTvr

class PrihodDocSerializer(DocSerializer):
    class Meta:
        exclude = ['typ']
        model = PrihodDoc

class PrihodTvrSerializer(TvrSerializer):
    class Meta:
        exclude = ['typ']
        model = PrihodTvr
