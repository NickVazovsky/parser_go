# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-20 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0002_prov'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='date_add',
        ),
    ]
