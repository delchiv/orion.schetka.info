# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20150416_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='prim',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
