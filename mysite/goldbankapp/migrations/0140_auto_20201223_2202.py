# Generated by Django 2.2.17 on 2020-12-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldbankapp', '0139_auto_20201223_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profiles_pic/demo_profile_pic2.jpg', upload_to='profiles_pic'),
        ),
    ]
