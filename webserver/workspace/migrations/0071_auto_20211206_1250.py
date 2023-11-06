# Generated by Django 3.1.13 on 2021-12-06 20:50
# (c) Meta Platforms, Inc. and affiliates. Copyright

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0070_auto_20211206_0817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesspointsector',
            old_name='distance',
            new_name='radius',
        ),
        migrations.AlterField(
            model_name='accesspointsector',
            name='azimuth',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1, message='Ensure this value is greater than or equal to %(limit_value)s degrees.'), django.core.validators.MaxValueValidator(360, message='Ensure this value is less than or equal to %(limit_value)s degrees.')]),
        ),
    ]
