# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-23 09:41
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180223_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citydict',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='机构描述'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
