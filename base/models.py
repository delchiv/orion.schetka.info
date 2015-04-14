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

class SpTvr(models.Model):
    num  = models.IntegerField()
    name = models.CharField(max_length=150)
#    ctg  = models.ForeignKey(Ctg, blank=True, null=True)

    class Meta:
       verbose_name = "Товар"
       verbose_name_plural = "Справочник товаров"

    def __unicode__(self):
        return self.name