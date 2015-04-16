# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20150416_1055'),
        ('recept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptDoc',
            fields=[
            ],
            options={
                'verbose_name': '\u0420\u0435\u0446\u0435\u043f\u0442',
                'proxy': True,
                'verbose_name_plural': '\u0420\u0435\u0446\u0435\u043f\u0442',
            },
            bases=('base.typeddoc',),
        ),
        migrations.CreateModel(
            name='ReceptTvr',
            fields=[
            ],
            options={
                'verbose_name': '\u0420\u0435\u0446\u0435\u043f\u0442',
                'proxy': True,
                'verbose_name_plural': '\u0420\u0435\u0446\u0435\u043f\u0442',
            },
            bases=('base.typedtvr',),
        ),
    ]
