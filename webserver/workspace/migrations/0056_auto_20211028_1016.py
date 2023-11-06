# Generated by Django 3.1.13 on 2021-10-28 17:16
# (c) Meta Platforms, Inc. and affiliates. Copyright

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0055_auto_20211027_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesspointlocation',
            name='height',
            field=models.FloatField(default=30, validators=[django.core.validators.MinValueValidator(0.1, message='Ensure this value is greater than or equal to %(limit_value)s m.'), django.core.validators.MaxValueValidator(1000, message='Ensure this value is less than or equal to %(limit_value)s. m')]),
        ),
    ]
