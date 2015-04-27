# coding: utf-8

from django.db import models

from base.models import TypedSpTvr, TypedDoc, TypedTvr, TypedManager

# Create your models here.

class Product(TypedSpTvr):
    default_typ = 'Product'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        proxy = True


class Component(TypedSpTvr):
    default_typ = 'Component'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Компонент"
        verbose_name_plural = "Компоненты"
        proxy = True

class ReceptDoc(TypedDoc):
    default_typ = 'Recept'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепт"
        proxy = True

class ReceptTvr(TypedTvr):
    default_typ = 'Recept'
    objects = TypedManager(default_typ)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепт"
        proxy = True