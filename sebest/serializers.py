# coding: utf-8

from rest_framework import serializers

from base.serializers import DocSerializer, TvrSerializer

from .models import CenaDoc, ReceptTvrCalc

class CenaDocSerializer(DocSerializer):
    class Meta:
        exclude = ['typ']
        model = CenaDoc

class ReceptTvrCalcSerializer(TvrSerializer):
    cena_akt = serializers.FloatField(read_only=True)
    sum_akt  = serializers.FloatField(read_only=True)
    cena_ost = serializers.FloatField(read_only=True)
    sum_ost  = serializers.FloatField(read_only=True)

    class Meta:
        exclude = ['typ']
        model = ReceptTvrCalc
