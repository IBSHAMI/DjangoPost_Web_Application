# Generated by Django 4.1.2 on 2023-04-06 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_job_framework'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appliedjob',
            options={'ordering': ['-date_applied']},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='savedjob',
            options={'ordering': ['-date_saved']},
        ),
    ]
