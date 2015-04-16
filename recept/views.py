# coding: utf-8

from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product, Component, ReceptDoc, ReceptTvr
from .serializers import ProductSerializer, ComponentSerializer, ReceptDocSerializer, ReceptTvrSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ReceptDocViewSet(viewsets.ModelViewSet):
    queryset = ReceptDoc.objects.all()
    serializer_class = ReceptDocSerializer

class ReceptTvrViewSet(viewsets.ModelViewSet):
    queryset = ReceptTvr.objects.all()
    serializer_class = ReceptTvrSerializer
