# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180129_0422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('E', 'E-mail'), ('P', 'Telefone')], max_length=1)),
                ('value', models.CharField(max_length=255)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Speaker')),
            ],
        ),
    ]
