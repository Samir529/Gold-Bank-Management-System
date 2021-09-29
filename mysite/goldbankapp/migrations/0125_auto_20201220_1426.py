# Generated by Django 2.2.17 on 2020-12-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0124_auto_20201219_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='location',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='mobileNo',
            field=models.IntegerField(default='0', max_length=11),
        ),
    ]