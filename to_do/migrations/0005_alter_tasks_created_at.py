# Generated by Django 4.1.3 on 2022-11-19 23:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0004_alter_tasks_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 19, 23, 42, 43, 465812, tzinfo=datetime.timezone.utc)),
        ),
    ]
