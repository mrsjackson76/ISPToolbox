# Generated by Django 3.1.13 on 2021-10-08 21:44
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0048_add_index_fake'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='viewshedtile',
            unique_together={('x', 'y', 'zoom', 'viewshed')},
        ),
    ]
