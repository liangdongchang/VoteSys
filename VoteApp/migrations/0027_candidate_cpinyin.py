# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-30 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0026_chatrecord_crnickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='cPinyin',
            field=models.CharField(default='', max_length=20),
        ),
    ]