# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20170903_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='product_line',
            field=models.ManyToManyField(blank=True, to='asset.product_lines', verbose_name='产品线'),
        ),
    ]