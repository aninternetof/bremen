# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 14:52
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170119_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=redactor.fields.RedactorField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=redactor.fields.RedactorField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=redactor.fields.RedactorField(),
        ),
    ]