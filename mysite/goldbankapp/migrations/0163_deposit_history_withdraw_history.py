# Generated by Django 2.2.17 on 2020-12-28 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0162_auto_20201227_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='deposit_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='0', max_length=30)),
                ('email', models.EmailField(default='0', max_length=254)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.FloatField(default='0', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='withdraw_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='0', max_length=30)),
                ('email', models.EmailField(default='0', max_length=254)),
                ('currentdate', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.FloatField(default='0', max_length=30)),
            ],
        ),
    ]
