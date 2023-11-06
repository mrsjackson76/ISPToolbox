# Generated by Django 3.1.13 on 2021-12-03 23:48
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0060_buildingcoverage_cpe_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewshed',
            name='mode',
            field=models.CharField(choices=[('VISIBLE', 'Visible'), ('DEM', 'Dem'), ('GROUND', 'Ground'), ('NORMAL', 'Normal')], default='GROUND', max_length=20),
        ),
    ]
