# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tambola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='winners',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]