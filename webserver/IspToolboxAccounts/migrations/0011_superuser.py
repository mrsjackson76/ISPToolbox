# Generated by Django 3.1.13 on 2021-09-28 18:25
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IspToolboxAccounts', '0010_auto_20210729_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
            ],
            options={
                'verbose_name': 'Super User',
                'verbose_name_plural': 'Super Users',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('IspToolboxAccounts.user',),
        ),
    ]
