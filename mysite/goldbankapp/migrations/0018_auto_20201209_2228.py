# Generated by Django 2.2.17 on 2020-12-09 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0017_auto_20201209_2215'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='deposit',
            new_name='deposits',
        ),
    ]