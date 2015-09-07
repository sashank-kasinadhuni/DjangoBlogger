# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('upvotes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('blog', models.ForeignKey(to='blogs.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('last_login_time', models.DateTimeField(verbose_name=b'last login')),
                ('user_create_time', models.DateTimeField(verbose_name=b'date joined')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='blogs.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(to='blogs.User'),
        ),
    ]
