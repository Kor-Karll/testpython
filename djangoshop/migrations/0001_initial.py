# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-15 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustID', models.CharField(max_length=15)),
                ('CustName', models.TextField()),
                ('CustPwd', models.TextField()),
                ('CustType', models.CharField(max_length=1)),
            ],
        ),
    ]
