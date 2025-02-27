# Generated by Django 5.1.4 on 2025-02-05 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_alter_debt_deadline_alter_savingsgoal_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2025, 2, 5, 23, 48, 34, 290658, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='savingsgoal',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2025, 2, 5, 23, 48, 34, 291475, tzinfo=datetime.timezone.utc), help_text="When do you want to reach your saving's goal?"),
        ),
    ]
