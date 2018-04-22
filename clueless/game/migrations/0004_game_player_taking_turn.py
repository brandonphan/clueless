# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180418_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player_taking_turn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_taking_turn', to='game.Player'),
        ),
    ]
