# Generated by Django 3.1.1 on 2020-10-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Overlay', '0002_delete_overlay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('source_url', models.CharField(max_length=50)),
                ('source_layer', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
