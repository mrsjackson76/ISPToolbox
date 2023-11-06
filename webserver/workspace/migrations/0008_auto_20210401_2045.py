# Generated by Django 3.1.6 on 2021-04-01 20:45
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0007_auto_20210331_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptocpelink',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aptocpelink',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='aptocpelink',
            name='ap',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='workspace.accesspointlocation'),
        ),
        migrations.AlterField(
            model_name='aptocpelink',
            name='cpe',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='workspace.cpelocation'),
        ),
    ]
