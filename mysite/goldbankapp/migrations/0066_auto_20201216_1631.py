# Generated by Django 2.2.17 on 2020-12-16 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0065_auto_20201216_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceofgold',
            name='day',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
