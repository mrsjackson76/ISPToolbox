# Generated by Django 3.1.13 on 2021-10-12 03:50
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0050_merge_20211011_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticsevent',
            name='created_at',
            field=models.CharField(default=1634010645.2325053, max_length=255),
        ),
    ]
