# Generated by Django 2.2.17 on 2020-12-15 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0034_auto_20201216_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='username1',
        ),
    ]