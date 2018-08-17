# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BankAccount'),
        ),
    ]
