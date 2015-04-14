# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_sptvr'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpGrp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0433\u0440\u0443\u043f\u043f',
            },
        ),
        migrations.AddField(
            model_name='sptvr',
            name='grp',
            field=models.ForeignKey(blank=True, to='base.SpGrp', null=True),
        ),
    ]
