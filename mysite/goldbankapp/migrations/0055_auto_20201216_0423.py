# Generated by Django 2.2.17 on 2020-12-15 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0054_auto_20201216_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceofgold',
            name='day',
            field=models.DateField(blank=True, default=datetime.date(1111, 11, 11), null=True),
        ),
    ]
