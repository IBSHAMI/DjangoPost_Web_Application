# Generated by Django 4.1.2 on 2022-11-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_profile_pic_employeeprofile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='users/employee/profile_pics'),
        ),
    ]
