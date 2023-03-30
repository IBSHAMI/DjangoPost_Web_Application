# Generated by Django 4.1.2 on 2023-03-30 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_companyprofile_company_location'),
        ('jobs', '0011_alter_job_language_alter_job_number_of_positions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companyprofile'),
        ),
    ]
