# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('explaination', models.TextField()),
                ('awnser', models.TextField(default='Vraag nog niet beantwoord...')),
                ('color', models.CharField(default='Grey', choices=[('teal', 'Teal'), ('grey lighten-2', 'Grey'), ('red lighten-1', 'Red'), ('blue', 'Blue')], max_length=50)),
                ('catergory', models.CharField(default='Anders', choices=[('online_veiligheid', 'Online Veiligheid'), ('hoe', 'Hoe kan ik ...?/Hoe werkt ...?'), ('anders', 'Anders')], max_length=50)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
