# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 02:37
from __future__ import unicode_literals

import LinkAct.models
import datetime
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
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('creator', models.IntegerField()),
                ('participants', LinkAct.models.ListField(default=[])),
                ('locale', models.CharField(max_length=20)),
                ('theme', LinkAct.models.ListField(default=[])),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('introduction', models.TextField()),
                ('supporters', LinkAct.models.ListField(default=[])),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.IntegerField()),
                ('score', models.IntegerField()),
                ('content', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('friends', LinkAct.models.ListField(default=[])),
                ('website', models.URLField()),
                ('city', models.CharField(max_length=20)),
                ('head', models.IntegerField(default=-1)),
                ('participate_terminative_acts', LinkAct.models.ListField(default=[])),
                ('create_terminative_acts', LinkAct.models.ListField(default=[])),
                ('participate_ongoing_acts', LinkAct.models.ListField(default=[])),
                ('create_ongoing_acts', LinkAct.models.ListField(default=[])),
                ('commented_acts', LinkAct.models.ListField(default=[])),
                ('gender', models.CharField(max_length=20)),
                ('interests', LinkAct.models.ListField(default=[])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
