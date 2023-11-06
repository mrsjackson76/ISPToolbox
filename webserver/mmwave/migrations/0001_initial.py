# Generated by Django 3.1.1 on 2021-03-11 01:58
# (c) Meta Platforms, Inc. and affiliates. Copyright

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EPTLidarPointCloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8192)),
                ('id_num', models.IntegerField(blank=True, null=True)),
                ('count', models.BigIntegerField()),
                ('url', models.URLField()),
                ('boundary', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('srs', models.IntegerField()),
                ('high_resolution_boundary', django.contrib.gis.db.models.fields.GeometryField(blank=True, default=None, null=True, srid=4326)),
                ('date_time_added_to_isptoolbox', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TGLink',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tx', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('rx', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('fbid', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('freq', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LOSSummary',
            fields=[
            ],
            options={
                'verbose_name': 'LOS Summary',
                'verbose_name_plural': 'LOS Summary',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('mmwave.tglink',),
        ),
    ]
