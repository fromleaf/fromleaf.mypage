# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fromleaf_common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page_container', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.PageContainer')),
            ],
        ),
    ]
