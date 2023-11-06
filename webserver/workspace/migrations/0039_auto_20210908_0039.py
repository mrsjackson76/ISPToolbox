# Generated by Django 3.1.12 on 2021-09-08 00:39
# (c) Meta Platforms, Inc. and affiliates. Copyright

from django.db import migrations, models
import workspace.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0038_workspacemapsession_lock_dragging'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewshed',
            name='max_zoom',
            field=models.IntegerField(default=17, validators=[workspace.models.validators.validate_zoom_level]),
        ),
        migrations.AddField(
            model_name='viewshed',
            name='min_zoom',
            field=models.IntegerField(default=12, validators=[workspace.models.validators.validate_zoom_level]),
        ),
    ]
