# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_player_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='turn_state',
            field=models.IntegerField(default=1),
        ),
    ]
