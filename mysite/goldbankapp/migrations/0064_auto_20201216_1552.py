# Generated by Django 2.2.17 on 2020-12-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0063_auto_20201216_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceofgold',
            name='day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
