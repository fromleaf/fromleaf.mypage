# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fromleaf_aboutme', '0001_initial'),
        ('fromleaf_common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmepage',
            name='page_container',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.PageContainer'),
        ),
    ]
