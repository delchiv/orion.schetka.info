# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20150416_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='num',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tvr',
            name='num',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
