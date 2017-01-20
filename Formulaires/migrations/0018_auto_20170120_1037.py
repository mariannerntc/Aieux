# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-20 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulaires', '0017_recherche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recherche',
            name='rech_fam',
            field=models.CharField(blank=True, choices=[(b'Une personne', b'Une personne'), (b'Une famille', b'Une famille'), (b'Un document', b'Un document')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='recherche',
            name='rech_page',
            field=models.CharField(blank=True, choices=[(b'Une personne', b'Une personne'), (b'Une famille', b'Une famille'), (b'Un document', b'Un document')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='recherche',
            name='rech_pers',
            field=models.CharField(blank=True, choices=[(b'Une personne', b'Une personne'), (b'Une famille', b'Une famille'), (b'Un document', b'Un document')], max_length=10, null=True),
        ),
    ]
