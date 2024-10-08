# Generated by Django 4.2.16 on 2024-09-25 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_dateandtime_end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='booking_dateandtime_start'),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_dateandtime_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='booking_dateandtime_start'),
        ),
        migrations.AddField(
            model_name='booking',
            name='number_of_guests',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=2),
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='booking_dateandtime_start'),
            preserve_default=False,
        ),
    ]
