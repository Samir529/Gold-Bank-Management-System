# Generated by Django 2.2.17 on 2020-12-03 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
    ]