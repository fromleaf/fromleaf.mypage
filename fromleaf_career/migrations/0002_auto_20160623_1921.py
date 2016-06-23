# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fromleaf_career', '0001_initial'),
        ('fromleaf_common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='member_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.MemberInfo'),
        ),
        migrations.AddField(
            model_name='careerpage',
            name='page_container',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.PageContainer'),
        ),
    ]
