# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20150415_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='sptvr',
            name='izm',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sptvr',
            name='typ',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
