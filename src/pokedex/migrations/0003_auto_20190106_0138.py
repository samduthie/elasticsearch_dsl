# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-06 01:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='pokedex_id',
            new_name='pokedex_index',
        ),
    ]