# Generated by Django 4.1.2 on 2023-03-31 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_companyprofile_company_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='company_description',
        ),
    ]
