# Generated by Django 2.2.17 on 2020-12-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0075_auto_20201218_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankmoney',
            name='serial',
            field=models.FloatField(default='0', max_length=100),
        ),
    ]