# Generated by Django 3.1.13 on 2021-10-01 16:19
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0042_auto_20210924_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('sessionId', models.CharField(max_length=255)),
                ('eventType', models.CharField(max_length=255)),
            ],
        ),
    ]
