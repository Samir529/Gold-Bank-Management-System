# Generated by Django 2.2.17 on 2020-12-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0026_remove_deposit_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='username',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='balance',
            field=models.FloatField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='email',
            field=models.EmailField(default='0', max_length=254),
        ),
    ]