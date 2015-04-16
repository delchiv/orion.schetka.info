# coding: utf-8

from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from recept.models import ReceptTvr
from recept.serializers import ReceptTvrSerializer

from .models import CenaDoc
from .serializers import CenaDocSerializer

# Create your views here.

class SebestViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = ReceptTvr.objects.all()
        serializer = ReceptTvrSerializer(queryset, many=True)
        return Response(serializer.data)

class CenaDocViewSet(viewsets.ModelViewSet):
    queryset = CenaDoc.objects.all()
    serializer_class = CenaDocSerializer
