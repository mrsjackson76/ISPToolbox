# Generated by Django 3.1.1 on 2021-03-11 01:58
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=63)),
                ('source_country', models.CharField(max_length=2)),
                ('last_updated', models.DateField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('source_id', 'source_country')},
            },
        ),
    ]
