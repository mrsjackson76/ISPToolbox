# Generated by Django 3.1.14 on 2022-04-07 18:57
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0102_delete_asynctaskapimodel'),
        ('api', '0003_dummytaskmodel_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummytaskmodel',
            name='ap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.accesspointlocation'),
        ),
    ]
