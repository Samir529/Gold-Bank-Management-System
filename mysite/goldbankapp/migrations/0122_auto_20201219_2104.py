# Generated by Django 2.2.17 on 2020-12-19 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0121_auto_20201219_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='last_withdraw_amount',
            field=models.FloatField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='loan',
            name='return_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]