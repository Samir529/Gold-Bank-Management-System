# Generated by Django 2.2.17 on 2020-12-15 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0037_userprofileinfo_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='password',
        ),
    ]