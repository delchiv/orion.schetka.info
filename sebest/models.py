# coding: utf-8

from django.db import models

from base.models import TypedDoc, TypedManager

# Create your models here.

class CenaDoc(TypedDoc):
    default_typ = 'Cena'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Актуальная цена"
        verbose_name_plural = "Актуальные цены"
        proxy = True

