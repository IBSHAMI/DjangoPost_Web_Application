import os
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create Company Profile after user is created
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    company_website = models.URLField(max_length=200, blank=True, null=True)
    company_size = models.CharField(max_length=10, blank=True, null=True)
    company_logo = models.ImageField(upload_to='users/company/logos', blank=True, null=True)
    company_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email

    def get_company_logo_filename(self):
        if self.company_logo:
            return os.path.basename(self.company_logo.name)
        return ""


# create user paypal account after user is created
def post_save_user_create_paypal_account(sender, instance, created, *args, **kwargs):
    # if user is created, add company profile to the user account
    if created:
        # Create Company Profile
        CompanyProfile.objects.create(user=instance)


post_save.connect(post_save_user_create_paypal_account, sender=User)
