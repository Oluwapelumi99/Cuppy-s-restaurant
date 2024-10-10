# Generated by Django 4.2.16 on 2024-10-10 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0030_alter_booking_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 13, 21, 20, 15, 871402)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_guests',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='2', max_length=6),
        ),
    ]
