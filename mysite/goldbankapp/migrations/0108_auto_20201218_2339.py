# Generated by Django 2.2.17 on 2020-12-18 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0107_auto_20201218_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceofgold',
            name='day',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]