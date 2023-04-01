import os
from django.db import models
from django.core.validators import URLValidator, MaxLengthValidator
from django.db.models.signals import post_save
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create employee profile after user is created
class EmployeeProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_profile')
    experience = models.CharField(max_length=100, blank=True, null=True)
    expected_salary = models.CharField(max_length=100, blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    portfolio_url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
    resume = models.FileField(upload_to='users/employee/resumes', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/employee/profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.email

    def get_resume_filename(self):
        if self.resume:
            return os.path.basename(self.resume.name)
        return ""

    def get_profile_picture_filename(self):
        if self.profile_picture:
            return os.path.basename(self.profile_picture.name)
        return ""


# Create user employee profile after user is created
def post_save_user_create_paypal_account(sender, instance, created, *args, **kwargs):
    # if user is created, add paypal payment account
    if created:
        # Create Employee Profile
        EmployeeProfile.objects.create(user=instance)


post_save.connect(post_save_user_create_paypal_account, sender=User)
