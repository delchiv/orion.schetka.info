# coding: utf-8

from rest_framework import serializers

from base.serializers import DocSerializer

from .models import CenaDoc

class CenaDocSerializer(DocSerializer):
    class Meta:
        exclude = ['typ']
        model = CenaDoc
