# coding: utf-8

from django.db import models

from base.models import TypedDoc, TypedTvr, TypedManager
from recept.models import ReceptTvr

# Create your models here.

class CenaDoc(TypedDoc):
    default_typ = 'Cena'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Актуальная цена"
        verbose_name_plural = "Актуальные цены"
        proxy = True

class ReceptTvrCalc(ReceptTvr):
    @property
    def cena_akt(self):
        try: return CenaDoc.objects.filter(tvr_kt=self.tvr_kt).order_by('-date')[0].s
        except: return 0

    @property
    def sum_akt(self):
        try: return CenaDoc.objects.filter(tvr_kt=self.tvr_kt).order_by('-date')[0].s*self.k
        except: return 0

    @property
    def cena_ost(self):
        return 0

    @property
    def sum_ost(self):
        return 0

    class Meta:
        proxy = True
