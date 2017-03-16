# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepoStarring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_username', models.CharField(max_length=39)),
                ('repo_owner_username', models.CharField(max_length=39)),
                ('repo_owner_type', models.CharField(max_length=16)),
                ('repo_name', models.CharField(max_length=100)),
                ('repo_full_name', models.CharField(max_length=140)),
                ('repo_url', models.URLField()),
                ('repo_language', models.CharField(max_length=32)),
                ('repo_description', models.CharField(max_length=191)),
                ('repo_created_at', models.DateTimeField()),
                ('repo_updated_at', models.DateTimeField()),
                ('stargazers_count', models.PositiveIntegerField()),
                ('forks_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_username', models.CharField(max_length=39)),
                ('to_username', models.CharField(max_length=39)),
                ('relation', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userrelation',
            unique_together=set([('from_username', 'relation', 'to_username')]),
        ),
        migrations.AlterUniqueTogether(
            name='repostarring',
            unique_together=set([('from_username', 'repo_full_name')]),
        ),
    ]