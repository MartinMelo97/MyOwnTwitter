# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='back_img',
            field=models.ImageField(blank=True, null=True, upload_to='user/%Y/%m/%d/back'),
        ),
    ]
