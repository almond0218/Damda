# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0002_bookmark_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='folderName',
            field=models.CharField(default='', max_length=20),
        ),
    ]
