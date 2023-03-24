from django.db import models

# import user model from settings
from django.conf import settings

user = settings.AUTH_USER_MODEL


class Job(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    number_of_positions = models.PositiveIntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    remote = models.BooleanField(default=False)
    salary = models.PositiveIntegerField(blank=True, null=True)

    internal = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
