# Generated by Django 4.1.2 on 2022-11-01 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_profile_pic_employeeprofile_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]