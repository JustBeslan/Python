# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200313_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField(verbose_name='Первое имя')),
                ('second_name', models.TextField(verbose_name='Второе имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.IntegerField(default=0, verbose_name='Лайков'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
