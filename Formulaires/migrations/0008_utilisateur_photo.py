# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulaires', '0007_auto_20170120_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'img/'),
        ),
    ]