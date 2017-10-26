# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 23:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='user',
        ),
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='sem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exam',
            name='marks_obt',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
