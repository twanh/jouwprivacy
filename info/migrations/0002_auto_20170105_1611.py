# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=10, choices=[('tip', 'Tip'), ('trick', 'Trick'), ('bescherm', 'Bescherm Jezelf'), ('hoe', 'Hoe kan iets?'), ('uitleg', 'Uitleg')], default='Tip'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.CharField(max_length=500, default=''),
        ),
    ]
