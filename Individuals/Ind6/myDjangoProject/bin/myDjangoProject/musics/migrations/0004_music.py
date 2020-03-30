# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-26 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_musicstyle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название ')),
                ('description', models.TextField(verbose_name='Описание')),
                ('musicStyle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musics.MusicStyle', verbose_name='Стиль ')),
                ('musician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musics.Musician', verbose_name='Автор ')),
            ],
        ),
    ]