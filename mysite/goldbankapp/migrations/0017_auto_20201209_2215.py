# Generated by Django 2.2.17 on 2020-12-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0016_auto_20201209_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='balance',
            field=models.FloatField(default='0', max_length=30),
        ),
    ]