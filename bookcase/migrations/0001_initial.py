# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-02 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_case', models.IntegerField(choices=[(1, 'Computer Science'), (2, 'Religion'), (3, 'Philosophy'), (4, 'Laws')])),
            ],
        ),
    ]
