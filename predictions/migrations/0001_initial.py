# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 17:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPA', models.FloatField(blank=True, default=None, null=True)),
                ('TOFEL', models.FloatField(blank=True, default=None, null=True)),
                ('SATI', models.FloatField(blank=True, default=None, null=True)),
                ('SchoolRankGroup', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('Admission', models.IntegerField(choices=[(1, 'Admit'), (2, 'Deny'), (3, 'Unknown')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]