# Generated by Django 3.1.8 on 2021-04-20 20:21
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmwave', '0006_auto_20210420_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usgslidarmetadatamodel',
            name='seamless_reason',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
