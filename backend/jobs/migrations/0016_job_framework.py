# Generated by Django 4.1.2 on 2023-04-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_alter_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='framework',
            field=models.CharField(blank=True, default='Django', max_length=100, null=True),
        ),
    ]