# Generated by Django 2.2.17 on 2020-12-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0045_auto_20201216_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='dateofbirth2',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
    ]
