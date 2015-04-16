# coding: utf-8

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class TypedManager(models.Manager):        
    def __init__(self, default_typ, *args, **kwargs):
        self.default_typ = default_typ
        super(TypedManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        return super(TypedManager, self).get_queryset().filter(typ=self.default_typ)


class Menu(MPTTModel):
    num  = models.IntegerField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['num']

    class Meta:
       verbose_name = 'Меню'
       verbose_name_plural = 'Меню'

    def __unicode__(self):
        return self.name


class SpGrp(models.Model):
    num  = models.IntegerField()
    name = models.CharField(max_length=150)

    class Meta:
       verbose_name = 'Группа'
       verbose_name_plural = 'Справочник групп'

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
       verbose_name = 'Товар'
       verbose_name_plural = 'Справочник товаров'

    def __unicode__(self):
        return self.name



class TypedSpTvr(SpTvr):
    default_typ = ''
    objects = TypedManager(default_typ)

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.typ = self.default_typ
        super(TypedSpTvr, self).save(*args, **kwargs)


class SpOrg(models.Model):
    num    = models.IntegerField()
    name   = models.CharField(max_length=150)

    typ    = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
       verbose_name = 'Организация'
       verbose_name_plural = 'Справочник организаций'

    def __unicode__(self):
        return self.name


class TypedSpOrg(SpOrg):
    default_typ = ''
    objects = TypedManager(default_typ)

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.typ = self.default_typ
        super(TypedSpOrg, self).save(*args, **kwargs)


class Doc(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    num  = models.CharField(max_length=50, blank=True, null=True)
    org_dt = models.ForeignKey(SpOrg, related_name='+', blank=True, null=True)
    org_kt = models.ForeignKey(SpOrg, related_name='+', blank=True, null=True)
    tvr_dt = models.ForeignKey(SpTvr, related_name='+', blank=True, null=True)
    tvr_kt = models.ForeignKey(SpTvr, related_name='+', blank=True, null=True)
    s    = models.FloatField(default=0)
    prim = models.CharField(max_length=150, blank=True, null=True)

    typ    = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
       verbose_name = 'Документ'
       verbose_name_plural = 'Документы'
       ordering = ['date']


class TypedDoc(Doc):
    default_typ = ''
    objects = TypedManager(default_typ)

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.typ = self.default_typ
        super(TypedDoc, self).save(*args, **kwargs)


class Tvr(models.Model):
    doc  = models.ForeignKey(Doc)
    num  = models.CharField(max_length=50, blank=True, null=True)
    tvr_dt = models.ForeignKey(SpTvr, related_name='+', blank=True, null=True)
    tvr_kt = models.ForeignKey(SpTvr, related_name='+', blank=True, null=True)
    k    = models.FloatField(default=0)
    c    = models.FloatField(default=0)
    s    = models.FloatField(default=0)

    typ    = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
       verbose_name = 'Товар'
       verbose_name_plural = 'Товары'


class TypedTvr(Tvr):
    default_typ = ''
    objects = TypedManager(default_typ)

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.typ = self.default_typ
        super(TypedTvr, self).save(*args, **kwargs)


class Prov(models.Model):
    doc  = models.ForeignKey(Doc)
    tvr  = models.ForeignKey(Tvr)

    date = models.DateField()
    num  = models.CharField(max_length=50)
    org_dt = models.ForeignKey(SpOrg, related_name='+', blank=True, null=True)
    org_kt = models.ForeignKey(SpOrg, related_name='+', blank=True, null=True)
    tvr_dt = models.ForeignKey(SpTvr, related_name='+', blank=True, null=True)
    tvr_kt = models.ForeignKey(SpTvr, related_name='+', blank=True, null=True)
    k    = models.FloatField(default=0)
    c    = models.FloatField(default=0)
    s    = models.FloatField(default=0)
    prim = models.CharField(max_length=150)

    typ    = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
       verbose_name = 'Проводка'
       verbose_name_plural = 'Проводки'


class TypedProv(Prov):
    default_typ = ''
    objects = TypedManager(default_typ)

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.typ = self.default_typ
        super(TypedProv, self).save(*args, **kwargs)

