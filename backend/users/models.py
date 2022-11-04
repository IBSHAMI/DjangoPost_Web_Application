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


# create user paypal account after user is created
def post_save_user_create_paypal_account(sender, instance, created, *args, **kwargs):
    # if user is created, add paypal payment account
    if created:
        # Create Company Profile
        CompanyProfile.objects.create(user=instance)
        # Create PayPal Account
        PayPalAccount.objects.create(user=instance,
                                     paypal_email=instance.email,
                                     paypal_phone_number=instance.phone_number)


post_save.connect(post_save_user_create_paypal_account, sender=User)
