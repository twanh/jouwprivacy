# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('color', models.CharField(max_length=50, default='Grey', choices=[('teal', 'Teal'), ('grey lighten-2', 'Grey'), ('red lighten-1', 'Red'), ('blue', 'Blue')])),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
