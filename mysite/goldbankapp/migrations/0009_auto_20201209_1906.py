# Generated by Django 2.2.17 on 2020-12-09 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0008_userprofileinfo_currentdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Retype_password', models.CharField(default='0', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='goldbankapp.User'),
        ),
    ]
