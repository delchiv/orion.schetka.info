# coding: utf-8

from base.models import TypedDoc, TypedTvr, TypedManager

# Create your models here.

class PrihodDoc(TypedDoc):
    default_typ = 'Raw_Prihod'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Покупка сырья"
        verbose_name_plural = "Покупка сырья"
        proxy = True

class PrihodTvr(TypedTvr):
    default_typ = 'Raw_Prihod'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Покупка сырья"
        verbose_name_plural = "Покупка сырья"
        proxy = True