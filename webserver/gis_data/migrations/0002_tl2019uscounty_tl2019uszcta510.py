# Generated by Django 3.1.6 on 2021-03-25 01:04
# (c) Meta Platforms, Inc. and affiliates. Copyright

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tl2019UsCounty',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('statefp', models.CharField(blank=True, max_length=2, null=True)),
                ('countyfp', models.CharField(blank=True, max_length=3, null=True)),
                ('countyns', models.CharField(blank=True, max_length=8, null=True)),
                ('geoid', models.CharField(blank=True, max_length=5, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('namelsad', models.CharField(blank=True, max_length=100, null=True)),
                ('lsad', models.CharField(blank=True, max_length=2, null=True)),
                ('classfp', models.CharField(blank=True, max_length=2, null=True)),
                ('mtfcc', models.CharField(blank=True, max_length=5, null=True)),
                ('csafp', models.CharField(blank=True, max_length=3, null=True)),
                ('cbsafp', models.CharField(blank=True, max_length=5, null=True)),
                ('metdivfp', models.CharField(blank=True, max_length=5, null=True)),
                ('funcstat', models.CharField(blank=True, max_length=1, null=True)),
                ('aland', models.FloatField(blank=True, null=True)),
                ('awater', models.FloatField(blank=True, null=True)),
                ('intptlat', models.CharField(blank=True, max_length=11, null=True)),
                ('intptlon', models.CharField(blank=True, max_length=12, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('geog', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, geography=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'tl_2019_us_county',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tl2019UsZcta510',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('zcta5ce10', models.CharField(blank=True, max_length=5, null=True)),
                ('geoid10', models.CharField(blank=True, max_length=5, null=True)),
                ('classfp10', models.CharField(blank=True, max_length=2, null=True)),
                ('mtfcc10', models.CharField(blank=True, max_length=5, null=True)),
                ('funcstat10', models.CharField(blank=True, max_length=1, null=True)),
                ('aland10', models.FloatField(blank=True, null=True)),
                ('awater10', models.FloatField(blank=True, null=True)),
                ('intptlat10', models.CharField(blank=True, max_length=11, null=True)),
                ('intptlon10', models.CharField(blank=True, max_length=12, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'tl_2019_us_zcta510',
                'managed': False,
            },
        ),
    ]
