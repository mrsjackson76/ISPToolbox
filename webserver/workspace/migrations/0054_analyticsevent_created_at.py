# Generated by Django 3.1.13 on 2021-10-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0053_remove_analyticsevent_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticsevent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
