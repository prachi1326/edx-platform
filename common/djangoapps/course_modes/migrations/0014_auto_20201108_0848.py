# Generated by Django 2.2.16 on 2020-11-08 08:48

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0013_auto_20200115_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemode',
            name='suggested_prices',
            field=models.CharField(blank=True, default='', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='coursemodesarchive',
            name='suggested_prices',
            field=models.CharField(blank=True, default='', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='historicalcoursemode',
            name='suggested_prices',
            field=models.CharField(blank=True, default='', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
