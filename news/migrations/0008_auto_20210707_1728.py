# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-07 14:28
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20210707_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]