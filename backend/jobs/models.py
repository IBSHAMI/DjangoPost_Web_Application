from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

from company.models import CompanyProfile
from employee.models import EmployeeProfile


class JobManager(models.Manager):
    # function that create jobs from the scraped data
    def create_jobs(self, jobs_data, job_title, searched_location):
        for job in jobs_data:
            # double check if job have a description
            if 'description' in job:
                job_instance, created = self.get_or_create(
                    title=job['title'],
                    job_id=job['id'],
                    defaults={
                        'job_company': job['company'],
                        'description': job['description'],
                        'location': searched_location,
                        'framework': job_title,  # the job title used to search will be the framework
                        'date_created': timezone.now(),
                        'internal': True,
                        'job_link': job['job_url'],
                        'is_active': True
                    }
                )
                if created:
                    print(f"Created job with id: {job_instance.id}")
                else:
                    print(f"Job with id: {job_instance.id} already exists")

    # function that delete old jobs
    def delete_old_jobs(self, days):
        # get all jobs that are older than 7 days, only internal jobs
        old_jobs = self.filter(date_created__lte=datetime.now() - timedelta(days=days), internal=True)
        # delete all old jobs
        old_jobs.delete()
        print(f"Deleted {len(old_jobs)} jobs")


class Job(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True, default='Full Time')
    framework = models.CharField(max_length=100, blank=True, null=True, default='Django')
    language = models.CharField(max_length=100, blank=True, null=True, default='English')
    experience = models.CharField(max_length=100, blank=True, null=True)
    number_of_positions = models.PositiveIntegerField(blank=True, null=True, default=1)

    date_created = models.DateTimeField(auto_now_add=True)

    remote = models.BooleanField(default=False)
    salary = models.CharField(max_length=100, blank=True, null=True)

    internal = models.BooleanField(default=False)

    # special fields for jobs that are scraped from indeed
    job_id = models.CharField(max_length=100, blank=True, null=True)
    job_link = models.CharField(max_length=1000, blank=True, null=True)
    job_company = models.CharField(max_length=300, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    objects = JobManager()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class SavedJob(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} saved {self.job.title}"

    class Meta:
        unique_together = ('employee', 'job')
        ordering = ['-date_saved']


class AppliedJob(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=100, blank=True, null=True, default='Applied')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} applied to {self.job.title}"

    class Meta:
        unique_together = ('employee', 'job')
        ordering = ['-date_applied']
