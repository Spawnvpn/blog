# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160326_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
