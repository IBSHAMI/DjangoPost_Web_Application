import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db.models.signals import post_save


# custom user model
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField("Phone number", unique=True, max_length=15, blank=True, null=True)
    user_creation_date = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('MYR', 'MYR'),
)


# Create employee profile after user is created
class EmployeeProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_profile')
    software_field = models.CharField(max_length=100, blank=True, null=True)
    expected_salary = models.IntegerField(blank=True, null=True)
    expected_salary_currency = models.CharField(max_length=100, blank=True, null=True, choices=CURRENCY_CHOICES)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    Portfolio_url = models.URLField(max_length=200, blank=True, null=True)
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


# Create Company Profile after user is created
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    company_website = models.URLField(max_length=200, blank=True, null=True)
    company_logo = models.ImageField(upload_to='users/company/logos', blank=True, null=True)

    def __str__(self):
        return self.user.email


class PayPalAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='paypal_account')
    paypal_email = models.EmailField(blank=True, null=True)
    paypal_username = models.CharField(max_length=100, blank=True, null=True)
    paypal_phone_number = models.CharField(max_length=15, blank=True, null=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


# create user library after user is created
def post_save_user_create_paypal_account(sender, instance, created, *args, **kwargs):
    # if user is created, add paypal payment account
    if created:
        # Create Employee Profile
        EmployeeProfile.objects.create(user=instance)
        # Create Company Profile
        CompanyProfile.objects.create(user=instance)
        # Create PayPal Account
        PayPalAccount.objects.create(user=instance,
                                     paypal_email=instance.email,
                                     paypal_phone_number=instance.phone_number)


post_save.connect(post_save_user_create_paypal_account, sender=User)
