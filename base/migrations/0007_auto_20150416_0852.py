# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20150415_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('num', models.CharField(max_length=50)),
                ('s', models.FloatField(default=0)),
                ('prim', models.CharField(max_length=150)),
                ('typ', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Prov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('num', models.CharField(max_length=50)),
                ('k', models.FloatField(default=0)),
                ('c', models.FloatField(default=0)),
                ('s', models.FloatField(default=0)),
                ('prim', models.CharField(max_length=150)),
                ('typ', models.CharField(max_length=50, null=True, blank=True)),
                ('doc', models.ForeignKey(to='base.Doc')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0432\u043e\u0434\u043a\u0430',
                'verbose_name_plural': '\u041f\u0440\u043e\u0432\u043e\u0434\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='SpOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('typ', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='Tvr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.CharField(max_length=50)),
                ('k', models.FloatField(default=0)),
                ('c', models.FloatField(default=0)),
                ('s', models.FloatField(default=0)),
                ('typ', models.CharField(max_length=50, null=True, blank=True)),
                ('doc', models.ForeignKey(to='base.Doc')),
                ('tvr_dt', models.ForeignKey(related_name='+', blank=True, to='base.SpTvr', null=True)),
                ('tvr_kt', models.ForeignKey(related_name='+', blank=True, to='base.SpTvr', null=True)),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.AddField(
            model_name='prov',
            name='org_dt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpOrg', null=True),
        ),
        migrations.AddField(
            model_name='prov',
            name='org_kt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpOrg', null=True),
        ),
        migrations.AddField(
            model_name='prov',
            name='tvr',
            field=models.ForeignKey(to='base.Tvr'),
        ),
        migrations.AddField(
            model_name='prov',
            name='tvr_dt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpTvr', null=True),
        ),
        migrations.AddField(
            model_name='prov',
            name='tvr_kt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpTvr', null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='org_dt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpOrg', null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='org_kt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpOrg', null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='tvr_dt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpTvr', null=True),
        ),
        migrations.AddField(
            model_name='doc',
            name='tvr_kt',
            field=models.ForeignKey(related_name='+', blank=True, to='base.SpTvr', null=True),
        ),
        migrations.CreateModel(
            name='TypedDoc',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('base.doc',),
        ),
        migrations.CreateModel(
            name='TypedProv',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('base.prov',),
        ),
        migrations.CreateModel(
            name='TypedSpOrg',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('base.sporg',),
        ),
        migrations.CreateModel(
            name='TypedTvr',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('base.tvr',),
        ),
    ]
