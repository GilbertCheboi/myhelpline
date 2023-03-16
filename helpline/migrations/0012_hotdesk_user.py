# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-28 13:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpline', '0011_auto_20180828_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotdesk',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
