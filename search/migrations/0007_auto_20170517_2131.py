# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_delete_search'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Insert',
            new_name='Server',
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'get_latest_by': 'push_date', 'verbose_name_plural': 'Server'},
        ),
    ]