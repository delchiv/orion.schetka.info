# coding: utf-8

from django.db import models

from base.models import TypedSpTvr, TypedSpTvrManager

# Create your models here.

class Product(TypedSpTvr):
    default_typ = 'Product'
    objects = TypedSpTvrManager(default_typ)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        proxy = True


class Component(TypedSpTvr):
    default_typ = 'Component'
    objects = TypedSpTvrManager(default_typ)

    class Meta:
        verbose_name = "Компонент"
        verbose_name_plural = "Компоненты"
        proxy = True
