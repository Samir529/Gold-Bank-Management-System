# Generated by Django 2.2.17 on 2020-12-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0051_userprofileinfo_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceofgold',
            name='day',
            field=models.DateField(),
        ),
    ]