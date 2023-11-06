# Generated by Django 3.1.14 on 2022-01-20 18:25
# (c) Meta Platforms, Inc. and affiliates. Copyright

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0079_accesspointcoveragebuildings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesspointlocation',
            name='name',
            field=models.CharField(default='Unnamed Tower', max_length=50, validators=[django.core.validators.MinLengthValidator(1, message='Ensure this value has length of at least %(limit_value)s characters.'), django.core.validators.MaxLengthValidator(50, message='Ensure this value has length at most %(limit_value)s characters.')]),
        ),
    ]
