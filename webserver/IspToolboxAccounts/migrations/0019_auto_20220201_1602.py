# Generated by Django 3.1.14 on 2022-02-02 00:02
# (c) Meta Platforms, Inc. and affiliates. Copyright

import IspToolboxAccounts.models.user_models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IspToolboxAccounts', '0018_auto_20211215_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', IspToolboxAccounts.models.user_models.IspToolboxUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='IspToolboxGuestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guest+', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
                'ordering': ['-created_at'],
            },
        ),
    ]
