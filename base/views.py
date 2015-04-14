# coding: utf-8

from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Menu, SpTvr, SpGrp
from .serializers import MenuSerializer, SpTvrSerializer, SpGrpSerializer

# Create your views here.

class ExtJSModelViewSet(viewsets.ModelViewSet):
    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'results':serializer.data, 'success':True, 'message':''}, status=status.HTTP_201_CREATED)
        return Response({'results':[], 'success':False, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class MenuViewSet(ExtJSModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SpTvrViewSet(ExtJSModelViewSet):
    queryset = SpTvr.objects.all()
    serializer_class = SpTvrSerializer

class SpGrpViewSet(ExtJSModelViewSet):
    queryset = SpGrp.objects.all()
    serializer_class = SpGrpSerializer
