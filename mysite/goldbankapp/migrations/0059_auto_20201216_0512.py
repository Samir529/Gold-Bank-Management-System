# Generated by Django 2.2.17 on 2020-12-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0058_auto_20201216_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='dateofbirth',
            field=models.DateField(),
        ),
    ]