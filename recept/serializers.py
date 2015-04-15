# coding: utf-8

from rest_framework import serializers

from base.serializers import SpTvrSerializer

from .models import Product, Component


class ProductSerializer(SpTvrSerializer):
    class Meta:
        exclude = ['typ']
        model = Product

class ComponentSerializer(SpTvrSerializer):
    class Meta:
        exclude = ['typ']
        model = Component

