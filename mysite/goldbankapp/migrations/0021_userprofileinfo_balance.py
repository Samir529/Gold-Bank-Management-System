# Generated by Django 2.2.17 on 2020-12-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0020_auto_20201209_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='balance',
            field=models.FloatField(default='0', max_length=30),
        ),
    ]
