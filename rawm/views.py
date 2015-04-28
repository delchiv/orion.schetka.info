# coding: utf-8

from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import PrihodDoc, PrihodTvr
from .serializers import PrihodDocSerializer, PrihodTvrSerializer

# Create your views here.

class PrihodDocViewSet(viewsets.ModelViewSet):
    queryset = PrihodDoc.objects.all()
    serializer_class = PrihodDocSerializer

class PrihodTvrViewSet(viewsets.ModelViewSet):
    queryset = PrihodTvr.objects.all()
    serializer_class = PrihodTvrSerializer
