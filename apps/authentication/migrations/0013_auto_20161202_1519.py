# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-02 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20160212_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertoken',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'created'),
        ),
    ]
