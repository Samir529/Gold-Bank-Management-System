# Generated by Django 2.2.17 on 2020-12-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0081_auto_20201218_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankmoney',
            name='abc',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
    ]
