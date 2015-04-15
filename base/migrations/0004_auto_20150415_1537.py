# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150414_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='sptvr',
            name='subgrp',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpGrp', null=True),
        ),
        migrations.AlterField(
            model_name='sptvr',
            name='grp',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpGrp', null=True),
        ),
    ]
