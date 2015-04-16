# coding: utf-8

from rest_framework import serializers

from base.serializers import SpTvrSerializer, DocSerializer, TvrSerializer

from .models import Product, Component, ReceptDoc, ReceptTvr


class ProductSerializer(SpTvrSerializer):
    class Meta:
        exclude = ['typ']
        model = Product

class ComponentSerializer(SpTvrSerializer):
    class Meta:
        exclude = ['typ']
        model = Component

class ReceptDocSerializer(DocSerializer):
    class Meta:
        exclude = ['typ']
        model = ReceptDoc

class ReceptTvrSerializer(TvrSerializer):
    class Meta:
        exclude = ['typ']
        model = ReceptTvr
