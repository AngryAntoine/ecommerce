# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170320_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to_featured)),
                ('title', models.CharField(blank=True, null=True, max_length=120)),
                ('text', models.CharField(blank=True, null=True, max_length=120)),
                ('text_right', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
