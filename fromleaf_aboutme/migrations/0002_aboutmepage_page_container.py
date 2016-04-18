# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fromleaf_common', '0001_initial'),
        ('fromleaf_aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmepage',
            name='page_container',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.PageContainer'),
        ),
    ]
