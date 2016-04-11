# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fromleaf_opening', '0001_initial'),
        ('fromleaf_common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplecomment',
            name='opening_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_opening.OpeningPage'),
        ),
        migrations.AddField(
            model_name='pagecontainer',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.UserInfo'),
        ),
        migrations.AddField(
            model_name='memberinfo',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.UserInfo'),
        ),
        migrations.AddField(
            model_name='extrauserinfo',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.UserInfo'),
        ),
    ]