# Generated by Django 4.1.2 on 2022-11-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_company_description_job_experience_job_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
