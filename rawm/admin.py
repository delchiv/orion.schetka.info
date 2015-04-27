# coding: utf-8

from django.contrib import admin

from .models import PrihodDoc, PrihodTvr

# Register your models here.

class PrihodTvrInline(admin.TabularInline):
    model = PrihodTvr
    extra = 0
    verbose_name = "Товар"
    verbose_name_plural = "Товары"

class PrihodAdmin(admin.ModelAdmin):
    inlines = [
        PrihodTvrInline,
    ]


admin.site.register(PrihodDoc, PrihodAdmin)

