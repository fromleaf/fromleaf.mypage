# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fromleaf_career.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('started_date', models.DateField()),
                ('finished_date', models.DateField(blank=True)),
                ('simple_description', models.CharField(blank=True, max_length=300)),
                ('description', models.CharField(blank=True, max_length=400)),
                ('company_image', models.ImageField(blank=True, upload_to=fromleaf_career.models.Company.get_upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('career_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_career.CareerPage')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('simple_description', models.CharField(blank=True, max_length=300)),
                ('duty_description', models.CharField(blank=True, max_length=300)),
                ('started_date', models.DateField()),
                ('finished_date', models.DateField(blank=True)),
                ('language', models.CharField(blank=True, max_length=200)),
                ('system', models.CharField(blank=True, max_length=200)),
                ('framework', models.CharField(blank=True, max_length=200)),
                ('architecture_image', models.ImageField(blank=True, upload_to=fromleaf_career.models.Project.get_upload_to)),
                ('architecture_describe', models.CharField(blank=True, max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_career.Company')),
            ],
        ),
    ]