# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usict', '0004_usersignup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='user_name',
            new_name='username',
        ),
    ]
