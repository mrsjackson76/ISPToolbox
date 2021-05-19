# Generated by Django 3.1.8 on 2021-05-19 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0013_workspacemapsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ptplink',
            name='network',
        ),
        migrations.AddField(
            model_name='accesspointlocation',
            name='session',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspace.workspacemapsession'),
        ),
        migrations.AddField(
            model_name='aptocpelink',
            name='session',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspace.workspacemapsession'),
        ),
        migrations.AddField(
            model_name='cpelocation',
            name='session',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspace.workspacemapsession'),
        ),
        migrations.DeleteModel(
            name='Network',
        ),
    ]
