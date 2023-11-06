# Generated by Django 3.1.13 on 2021-10-08 21:27
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmwave', '0018_lidardatasets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lidardsmtilemodel',
            name='x',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='lidardsmtilemodel',
            name='y',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='lidardsmtilemodel',
            name='zoom',
            field=models.IntegerField(db_index=True),
        ),
    ]
