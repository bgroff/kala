# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kala_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.Permission'),
        ),
    ]