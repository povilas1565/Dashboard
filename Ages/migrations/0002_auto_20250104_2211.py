# Generated by Django 3.0 on 2025-01-04 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agesverification',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='agesverification',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 4, 22, 11, 50, 698933)),
        ),
    ]
