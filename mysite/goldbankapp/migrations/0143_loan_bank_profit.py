# Generated by Django 2.2.17 on 2020-12-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0142_userprofileinfo_account_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='bank_profit',
            field=models.FloatField(default='0', max_length=30),
        ),
    ]
