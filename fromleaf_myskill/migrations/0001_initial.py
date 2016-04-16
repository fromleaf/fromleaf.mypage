# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 06:22
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
            name='MySkillPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page_container', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.PageContainer')),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kind', models.CharField(choices=[('DEVELOPMENT_TOOL', 'Development'), ('COOPERATION_TOOL', 'Cooperation'), ('OS', 'OS'), ('PERSONALITY', 'Personality'), ('ETC', 'etc')], max_length=20)),
                ('level', models.IntegerField()),
                ('describe', models.TextField(max_length=400)),
                ('my_skill_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_myskill.MySkillPage')),
            ],
        ),
    ]
