# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-06 01:40
from __future__ import unicode_literals

from django.db import migrations

import csv
from pokedex.models import Pokemon


def forwards(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    populate_pokemon()

        
def populate_pokemon():
    path = '/src/pokedex/migrations/'
    with open(path + 'pokemon.csv', 'r') as data_csv:
        
        next(data_csv) # skip titles

        data = csv.reader(data_csv)
        for row in data:
            number = row[0]
            name = row[1]
            type1 = row[2]
            type2 = row[3]

            total_stats = row[4]
            hp = row[5]
            attack = row[6]
            defense = row[7]
            special_attack = row[8]
            special_defense = row[9]
            Speed = row[10]

            generation = row[11]
            is_legendary = row[12]

            try:
                Pokemon.objects.create(
                	pokedex_index=number,
                    name=name,
                    type1=type1,
                    type2=type2,

                    total_stats=total_stats,
                    generation=generation,
                    is_legendary = is_legendary,
                )
            except Exception as e:
            	print("{} was not inserted into db".format(name))
            	print(e)

class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_auto_20190106_0138'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]