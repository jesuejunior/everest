# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 11:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'verbose_name': 'Container',
                'db_table': 'container',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('so', models.CharField(max_length=40)),
                ('provider', models.CharField(default='digital ocean', max_length=20)),
                ('ip', models.GenericIPAddressField()),
                ('fqdn', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=22)),
                ('private_key', models.CharField(max_length=200)),
                ('ready', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Node',
                'db_table': 'node',
            },
        ),
        migrations.CreateModel(
            name='Spacebus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('container', models.ManyToManyField(blank=True, db_table='spacebus_has_container', null=True, related_name='spacebus', to='engine.Container')),
            ],
            options={
                'verbose_name': 'Spacebus',
                'db_table': 'spacebus',
            },
        ),
    ]
