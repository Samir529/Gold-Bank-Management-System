# Generated by Django 2.2.17 on 2020-12-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0066_auto_20201216_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='accNo',
            field=models.CharField(default='0', max_length=6),
        ),
    ]
