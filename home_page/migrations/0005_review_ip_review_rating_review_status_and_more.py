# Generated by Django 4.2.16 on 2024-09-26 11:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_delete_customemailconfirmationview'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
