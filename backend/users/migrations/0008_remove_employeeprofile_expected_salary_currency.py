# Generated by Django 4.1.2 on 2022-11-02 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_portfolio_url_employeeprofile_portfolio_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='expected_salary_currency',
        ),
    ]