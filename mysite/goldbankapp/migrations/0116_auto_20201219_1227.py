# Generated by Django 2.2.17 on 2020-12-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0115_deposit_withdrawdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='withdrawdate',
            field=models.DateField(default='no withdraw yet'),
        ),
    ]
