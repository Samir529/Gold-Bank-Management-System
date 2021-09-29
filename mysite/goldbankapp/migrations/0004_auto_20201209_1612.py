# Generated by Django 2.2.17 on 2020-12-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0003_account_priceofgold'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='email',
            field=models.EmailField(default='0', max_length=254),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='first_name',
            field=models.CharField(default='0', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='last_name',
            field=models.CharField(default='0', max_length=128),
        ),
    ]