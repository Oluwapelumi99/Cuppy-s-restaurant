# Generated by Django 5.1.1 on 2024-10-02 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_booking_customer_booking_deadline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='deadline',
        ),
    ]
