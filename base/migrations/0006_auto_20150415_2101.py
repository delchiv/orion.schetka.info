# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20150415_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypedSpTvr',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('base.sptvr',),
        ),
        migrations.AlterField(
            model_name='sptvr',
            name='izm',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sptvr',
            name='typ',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
