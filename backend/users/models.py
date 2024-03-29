import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.core.validators import EmailValidator
from django.db.models.signals import post_save


# custom user model
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, validators=[EmailValidator()])
    phone_number = models.CharField("Phone number", unique=True, max_length=15, blank=True, null=True)
    user_creation_date = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


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
        # Create PayPal Account
        PayPalAccount.objects.create(user=instance,
                                     paypal_email=instance.email,
                                     paypal_phone_number=instance.phone_number)


post_save.connect(post_save_user_create_paypal_account, sender=User)
