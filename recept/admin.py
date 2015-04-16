# coding: utf-8

from django.contrib import admin

from .models import Component, Product, ReceptDoc, ReceptTvr

# Register your models here.

class ReceptTvrInline(admin.TabularInline):
    model = ReceptTvr
    extra = 0
    verbose_name = "Компонент"
    verbose_name_plural = "Компоненты"

class ReceptAdmin(admin.ModelAdmin):
    inlines = [
        ReceptTvrInline,
    ]


admin.site.register(Component)
admin.site.register(Product)
admin.site.register(ReceptDoc, ReceptAdmin)

