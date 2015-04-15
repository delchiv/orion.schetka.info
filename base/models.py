# coding: utf-8

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Menu(MPTTModel):
    num  = models.IntegerField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['num']

    class Meta:
       verbose_name = "Меню"
       verbose_name_plural = "Меню"

    def __unicode__(self):
        return self.name


class SpGrp(models.Model):
    num  = models.IntegerField()
    name = models.CharField(max_length=150)

    class Meta:
       verbose_name = "Группа"
       verbose_name_plural = "Справочник групп"

    def __unicode__(self):
        return self.name


class SpTvr(models.Model):
    num    = models.IntegerField()
    name   = models.CharField(max_length=150)
    izm    = models.CharField(max_length=20, blank=True, null=True)
    grp    = models.ForeignKey(SpGrp, related_name='+', blank=True, null=True)
    subgrp = models.ForeignKey(SpGrp, related_name='+', blank=True, null=True)

    typ    = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
       verbose_name = "Товар"
       verbose_name_plural = "Справочник товаров"

    def __unicode__(self):
        return self.name

class TypedSpTvrManager(models.Manager):        
    def __init__(self, default_typ, *args, **kwargs):
        self.default_typ = default_typ
        super(TypedSpTvrManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        return super(TypedSpTvrManager, self).get_queryset().filter(typ=self.default_typ)

class TypedSpTvr(SpTvr):
    default_typ = ''
    objects = TypedSpTvrManager(default_typ)

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.typ = self.default_typ
        super(TypedSpTvr, self).save(*args, **kwargs)
