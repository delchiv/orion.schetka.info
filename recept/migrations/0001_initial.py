# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20150415_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442',
                'proxy': True,
                'verbose_name_plural': '\u041a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u044b',
            },
            bases=('base.typedsptvr',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'proxy': True,
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
            bases=('base.typedsptvr',),
        ),
    ]
