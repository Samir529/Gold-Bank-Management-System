# Generated by Django 2.2.17 on 2020-12-15 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0040_auto_20201216_0332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='dateofbirth',
            new_name='dateofbirth2',
        ),
    ]
