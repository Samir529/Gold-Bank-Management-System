# Generated by Django 2.2.17 on 2020-12-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0109_auto_20201219_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceofgold',
            name='serial',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
    ]
