# Generated by Django 2.2.17 on 2020-12-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0147_auto_20201225_1708'),
    ]

    operations = [
        migrations.DeleteModel(
            name='account',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='acc_no',
            field=models.CharField(blank=True, default='-', max_length=30, null=True),
        ),
    ]
