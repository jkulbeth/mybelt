# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='users',
        ),
        migrations.RemoveField(
            model_name='item',
            name='wished',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
