# Generated by Django 4.1.2 on 2023-04-04 20:39

from django.db import migrations, models
import employee.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employeeprofile_expected_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=employee.models.get_resume_upload_path),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=employee.models.get_picture_upload_path),
        ),
    ]
