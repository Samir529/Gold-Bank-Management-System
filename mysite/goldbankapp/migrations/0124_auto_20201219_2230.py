# Generated by Django 2.2.17 on 2020-12-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0123_loan_return_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='gold_price_at_creation',
            field=models.FloatField(default='0.0', max_length=30),
        ),
        migrations.AddField(
            model_name='deposit',
            name='interest_balance',
            field=models.FloatField(default='0', max_length=30),
        ),
    ]
