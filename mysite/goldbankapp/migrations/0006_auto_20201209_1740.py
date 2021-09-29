# Generated by Django 2.2.17 on 2020-12-09 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0005_auto_20201209_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='nid',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='currentdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]