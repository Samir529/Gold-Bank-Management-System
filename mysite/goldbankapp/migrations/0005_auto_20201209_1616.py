# Generated by Django 2.2.17 on 2020-12-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0004_auto_20201209_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='nid',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='first_name',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='last_name',
            field=models.CharField(default='0', max_length=30),
        ),
    ]