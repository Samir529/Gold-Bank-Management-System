# Generated by Django 2.2.17 on 2020-12-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0157_auto_20201226_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='account_age',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]