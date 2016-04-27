# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fromleaf_common.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fromleaf_aboutme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kind', models.CharField(choices=[('ELEMENTARY_SCHOOL', 'Elementary School'), ('MIDDLE_SCHOOL', 'Middle School'), ('HIGH_SCHOOL', 'High School'), ('UNIVERSICY', 'University'), ('GRADUATE_SCHOOL', 'Graduate school')], max_length=50)),
                ('major', models.CharField(max_length=200, null=True)),
                ('score', models.FloatField(blank=True, default=0.0)),
                ('entranced_date', models.DateField(default='1980-01-01', null=True)),
                ('graduated_date', models.DateField(default='1980-01-01', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(default='1980-01-01')),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone_number', models.PositiveIntegerField(blank=True)),
                ('cellphone_number', models.PositiveIntegerField(blank=True)),
                ('profile_image', models.ImageField(blank=True, default='/media/photos/default/no_image.png', upload_to=fromleaf_common.models.user.ExtraUserInfo.get_upload_to)),
                ('blog_address', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('grade', models.CharField(choices=[('GUEST', 'Guest'), ('MEMBER', 'Member'), ('OWNER', 'Owner'), ('ADMIN', 'Administrator')], default='MEMBER', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='page_container', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('comment', models.TextField(help_text='Input Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('aboutme_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_aboutme.AboutMePage')),
            ],
        ),
        migrations.CreateModel(
            name='UserSNSInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sns_name', models.CharField(choices=[('FACEBOOK', 'Facebook'), ('GITHUB', 'Github'), ('LINKEDIN', 'Linkedin')], max_length=200)),
                ('sns_address', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=200)),
                ('extra_user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.ExtraUserInfo')),
            ],
        ),
    ]
