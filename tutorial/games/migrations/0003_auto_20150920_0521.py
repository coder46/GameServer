# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_pricing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gamePicUrl',
            field=models.URLField(default=b'http://www.google.com'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pic1Url',
            field=models.URLField(default=b'http://www.google.com'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pic2Url',
            field=models.URLField(default=b'http://www.google.com'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pic3Url',
            field=models.URLField(default=b'http://www.google.com'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pricing',
            field=models.FloatField(default=250.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
