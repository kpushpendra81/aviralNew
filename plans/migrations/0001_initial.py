# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-01 19:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advisorPlanDetail',
            fields=[
                ('PlanDetailId', models.AutoField(primary_key=True, serialize=False)),
                ('PlanName', models.CharField(max_length=10)),
                ('planDuration', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('interest', models.BooleanField(default=0.0)),
                ('target', models.BooleanField(default=0.0)),
                ('profit', models.BooleanField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='investerPlanDetail',
            fields=[
                ('PlanDetailId', models.AutoField(primary_key=True, serialize=False)),
                ('PlanName', models.CharField(max_length=10)),
                ('planDuration', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('interest', models.BooleanField(default=0.0)),
                ('profit', models.BooleanField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
