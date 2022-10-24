from django.contrib import admin
from .models import User, PayPalAccount

#  register the user and PaypalAccount model
admin.site.register(User)
admin.site.register(PayPalAccount)