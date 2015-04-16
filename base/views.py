# coding: utf-8

from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Menu, SpTvr, SpGrp, Tvr
from .serializers import MenuSerializer, SpTvrSerializer, SpGrpSerializer, TvrSerializer

# Create your views here.

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SpTvrViewSet(viewsets.ModelViewSet):
    queryset = SpTvr.objects.all()
    serializer_class = SpTvrSerializer


class SpGrpViewSet(viewsets.ModelViewSet):
    queryset = SpGrp.objects.all()
    serializer_class = SpGrpSerializer


class DocTvrViewSet(viewsets.ViewSet):

    def retrive(self, request, pk=None):
        queryset = Tvr.objects.filter(doc_id=pk)
        serializer = TvrSerializer(queryset, many=True)
        return Response(serializer.data)
