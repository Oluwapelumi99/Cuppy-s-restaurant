# Generated by Django 5.1.1 on 2024-10-01 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_booking_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(choices=[('1', 'Reserved'), ('2', 'Available')], default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.table'),
        ),
    ]
