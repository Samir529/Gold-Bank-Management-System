# Generated by Django 2.2.17 on 2020-12-23 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0143_loan_bank_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
