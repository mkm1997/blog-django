# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usict', '0010_auto_20171013_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
