# Generated by Django 3.1.14 on 2022-02-08 00:26
# (c) Meta Platforms, Inc. and affiliates. Copyright

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IspToolboxApp', '0006_standardizedmlabglobal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form477Dec2020',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logrecno', models.IntegerField(blank=True, null=True)),
                ('provider_id', models.IntegerField(blank=True, null=True)),
                ('frn', models.IntegerField(blank=True, null=True)),
                ('providername', models.CharField(blank=True, max_length=255, null=True)),
                ('dbaname', models.CharField(blank=True, max_length=255, null=True)),
                ('holdingcompanyname', models.CharField(blank=True, max_length=255, null=True)),
                ('hoconum', models.IntegerField(blank=True, null=True)),
                ('hocofinal', models.CharField(blank=True, max_length=255, null=True)),
                ('stateabbr', models.CharField(blank=True, max_length=20, null=True)),
                ('blockcode', models.CharField(blank=True, max_length=15, null=True)),
                ('techcode', models.IntegerField(blank=True, null=True)),
                ('consumer', models.IntegerField(blank=True, null=True)),
                ('maxaddown', models.FloatField(blank=True, null=True)),
                ('maxadup', models.FloatField(blank=True, null=True)),
                ('business', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form477dec2020',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Form477Jun2019',
            fields=[
                ('logrecno', models.AutoField(primary_key=True, serialize=False)),
                ('provider_id', models.IntegerField(blank=True, null=True)),
                ('frn', models.IntegerField(blank=True, null=True)),
                ('providername', models.CharField(blank=True, max_length=255, null=True)),
                ('dbaname', models.CharField(blank=True, max_length=255, null=True)),
                ('holdingcompanyname', models.CharField(blank=True, max_length=255, null=True)),
                ('hoconum', models.IntegerField(blank=True, null=True)),
                ('hocofinal', models.CharField(blank=True, max_length=255, null=True)),
                ('stateabbr', models.CharField(blank=True, max_length=20, null=True)),
                ('blockcode', models.CharField(blank=True, max_length=15, null=True)),
                ('techcode', models.IntegerField(blank=True, null=True)),
                ('consumer', models.IntegerField(blank=True, null=True)),
                ('maxaddown', models.FloatField(blank=True, null=True)),
                ('maxadup', models.FloatField(blank=True, null=True)),
                ('business', models.FloatField(blank=True, null=True)),
                ('maxcirdown', models.FloatField(blank=True, null=True)),
                ('maxcirup', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form477jun2019',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tl2019BlocksCensus',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('statefp10', models.CharField(blank=True, max_length=2, null=True)),
                ('countyfp10', models.CharField(blank=True, max_length=3, null=True)),
                ('tractce10', models.CharField(blank=True, max_length=6, null=True)),
                ('blockce10', models.CharField(blank=True, max_length=4, null=True)),
                ('geoid10', models.CharField(blank=True, max_length=15, null=True)),
                ('name10', models.CharField(blank=True, max_length=10, null=True)),
                ('mtfcc10', models.CharField(blank=True, max_length=5, null=True)),
                ('ur10', models.CharField(blank=True, max_length=1, null=True)),
                ('uace10', models.CharField(blank=True, max_length=5, null=True)),
                ('uatype', models.CharField(blank=True, max_length=1, null=True)),
                ('funcstat10', models.CharField(blank=True, max_length=1, null=True)),
                ('aland10', models.FloatField(blank=True, null=True)),
                ('awater10', models.FloatField(blank=True, null=True)),
                ('intptlat10', models.CharField(blank=True, max_length=11, null=True)),
                ('intptlon10', models.CharField(blank=True, max_length=12, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('geog', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, geography=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'tl_2019_blocks_census',
                'managed': False,
            },
        ),
    ]
