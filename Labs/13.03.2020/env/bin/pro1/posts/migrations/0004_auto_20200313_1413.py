# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Текст сообщения'),
        ),
    ]