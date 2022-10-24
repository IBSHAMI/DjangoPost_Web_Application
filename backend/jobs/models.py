from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)

    date_created = models.DateTimeField(auto_now_add=True)

    remote = models.BooleanField(default=False)
    salary = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
