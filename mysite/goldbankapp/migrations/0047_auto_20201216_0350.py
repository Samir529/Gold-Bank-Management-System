# Generated by Django 2.2.17 on 2020-12-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0046_auto_20201216_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='dateofbirth2',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]