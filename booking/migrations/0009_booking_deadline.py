# Generated by Django 5.1.1 on 2024-10-02 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_remove_booking_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 29, 12, 18, 27, 10051)),
        ),
    ]
