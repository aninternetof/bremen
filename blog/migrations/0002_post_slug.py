# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-23 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='not_set', max_length=100),
            preserve_default=False,
        ),
    ]
