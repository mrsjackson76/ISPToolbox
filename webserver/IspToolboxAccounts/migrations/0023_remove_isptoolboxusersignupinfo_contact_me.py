# Generated by Django 3.1.14 on 2022-06-08 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IspToolboxAccounts', '0022_auto_20220328_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isptoolboxusersignupinfo',
            name='contact_me',
        ),
    ]
