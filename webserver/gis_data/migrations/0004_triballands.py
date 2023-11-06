# Generated by Django 3.1.12 on 2021-06-23 02:51
# (c) Meta Platforms, Inc. and affiliates. Copyright

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_data', '0003_tl2020uscensusblocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='TribalLands',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('aiannhce', models.CharField(blank=True, max_length=4, null=True)),
                ('aiannhns', models.CharField(blank=True, max_length=8, null=True)),
                ('geoid', models.CharField(blank=True, max_length=5, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('namelsad', models.CharField(blank=True, max_length=100, null=True)),
                ('lsad', models.CharField(blank=True, max_length=2, null=True)),
                ('classfp', models.CharField(blank=True, max_length=2, null=True)),
                ('comptyp', models.CharField(blank=True, max_length=1, null=True)),
                ('aiannhr', models.CharField(blank=True, max_length=1, null=True)),
                ('mtfcc', models.CharField(blank=True, max_length=5, null=True)),
                ('funcstat', models.CharField(blank=True, max_length=1, null=True)),
                ('aland', models.FloatField(blank=True, null=True)),
                ('awater', models.FloatField(blank=True, null=True)),
                ('intptlat', models.CharField(blank=True, max_length=11, null=True)),
                ('intptlon', models.CharField(blank=True, max_length=12, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'tribal_lands',
                'managed': False,
            },
        ),
    ]
