# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('gamePicUrl', models.URLField()),
                ('pic1Url', models.URLField()),
                ('pic2Url', models.URLField()),
                ('pic3Url', models.URLField()),
                ('publisher', models.CharField(default=b'', max_length=100)),
                ('publishedDate', models.DateField()),
                ('ratedInfo', models.CharField(default=b'', max_length=100)),
                ('gameCats', models.CharField(default=b'', max_length=100)),
                ('trailerUrl', models.URLField()),
                ('buyUrl', models.URLField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'ordering': ('publishedDate',),
            },
        ),
    ]
