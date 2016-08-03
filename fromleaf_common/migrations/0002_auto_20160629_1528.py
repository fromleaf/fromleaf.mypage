# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 06:28
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
            name='member_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.MemberInfo'),
        ),
        migrations.AddField(
            model_name='extrauserinfo',
            name='member_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.MemberInfo'),
        ),
        migrations.AddField(
            model_name='education',
            name='extra_user_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fromleaf_common.ExtraUserInfo'),
        ),
    ]