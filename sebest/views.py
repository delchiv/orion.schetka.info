# coding: utf-8

from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import CenaDoc, ReceptTvrCalc
from .serializers import CenaDocSerializer, ReceptTvrCalcSerializer

# Create your views here.

class SebestViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = ReceptTvrCalc.objects.all()
        serializer = ReceptTvrCalcSerializer(queryset, many=True)
        return Response(serializer.data)

class CenaDocViewSet(viewsets.ModelViewSet):
    queryset = CenaDoc.objects.all()
    serializer_class = CenaDocSerializer
