# Generated by Django 2.2.17 on 2020-12-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0036_auto_20201216_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='password',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
