# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_buyevent_externalurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyevent',
            name='model_pic',
            field=models.ImageField(blank=True, upload_to='../media/'),
        ),
    ]
