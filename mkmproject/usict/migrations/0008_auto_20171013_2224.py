# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usict', '0007_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feedback',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
