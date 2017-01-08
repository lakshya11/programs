# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-04 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tambola', '0002_winners_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.IntegerField()),
                ('x1', models.IntegerField(max_length=50)),
                ('x2', models.IntegerField(max_length=50)),
                ('x3', models.IntegerField(max_length=50)),
                ('x4', models.IntegerField(max_length=50)),
                ('x5', models.IntegerField(max_length=50)),
                ('x6', models.IntegerField(max_length=50)),
                ('x7', models.IntegerField(max_length=50)),
                ('x8', models.IntegerField(max_length=50)),
                ('x9', models.IntegerField(max_length=50)),
                ('y1', models.IntegerField(max_length=50)),
                ('y2', models.IntegerField(max_length=50)),
                ('y3', models.IntegerField(max_length=50)),
                ('y4', models.IntegerField(max_length=50)),
                ('y5', models.IntegerField(max_length=50)),
                ('y6', models.IntegerField(max_length=50)),
                ('y7', models.IntegerField(max_length=50)),
                ('y8', models.IntegerField(max_length=50)),
                ('y9', models.IntegerField(max_length=50)),
                ('z1', models.IntegerField(max_length=50)),
                ('z2', models.IntegerField(max_length=50)),
                ('z3', models.IntegerField(max_length=50)),
                ('z4', models.IntegerField(max_length=50)),
                ('z5', models.IntegerField(max_length=50)),
                ('z6', models.IntegerField(max_length=50)),
                ('z7', models.IntegerField(max_length=50)),
                ('z8', models.IntegerField(max_length=50)),
                ('z9', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TicketsGenerated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tambola.Players')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tambola.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TicketsStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tambola.Players')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tambola.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TokensGenerated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='winners',
            name='username',
        ),
        migrations.AddField(
            model_name='winners',
            name='player',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='tambola.Players'),
            preserve_default=False,
        ),
    ]