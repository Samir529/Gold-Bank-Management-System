# Generated by Django 2.2.17 on 2020-12-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0135_auto_20201220_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='location',
            field=models.CharField(blank=True, default='-', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='mobileNo',
            field=models.CharField(blank=True, default='-', max_length=11, null=True),
        ),
    ]
