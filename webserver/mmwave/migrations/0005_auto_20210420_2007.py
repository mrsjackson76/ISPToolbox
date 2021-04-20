# Generated by Django 3.1.8 on 2021-04-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmwave', '0004_usgslidarmetadatamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usgslidarmetadatamodel',
            name='lpc_pub_date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usgslidarmetadatamodel',
            name='onemeter_reason',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usgslidarmetadatamodel',
            name='opr_pub_date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usgslidarmetadatamodel',
            name='spec',
            field=models.CharField(help_text='USGS lidar specification 1.0 - LAS1.2 if >USGS 1.0 - LAS1.4', max_length=255),
        ),
        migrations.AlterField(
            model_name='usgslidarmetadatamodel',
            name='workpackage',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
