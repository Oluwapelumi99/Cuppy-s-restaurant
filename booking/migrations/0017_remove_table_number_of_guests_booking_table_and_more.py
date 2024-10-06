# Generated by Django 5.1.1 on 2024-10-06 12:51

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_alter_booking_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='number_of_guests',
        ),
        migrations.AddField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.table'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 12, 51, 5, 852570)),
        ),
    ]
