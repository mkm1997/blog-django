# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usict', '0008_auto_20171013_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
