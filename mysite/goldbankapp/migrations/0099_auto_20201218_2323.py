# Generated by Django 2.2.17 on 2020-12-18 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0098_auto_20201218_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceofgold',
            name='day',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
