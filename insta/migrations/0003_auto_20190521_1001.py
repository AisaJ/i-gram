# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20190520_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='wink.png', upload_to='profile/'),
        ),
    ]