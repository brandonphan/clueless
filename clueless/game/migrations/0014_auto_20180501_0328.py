# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_suggestion_refuting_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stored_info', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='notebook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.Notebook'),
        ),
    ]
