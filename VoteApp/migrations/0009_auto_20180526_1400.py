# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-26 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0008_auto_20180526_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uPass',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]