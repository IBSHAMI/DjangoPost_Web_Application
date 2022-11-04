from django.contrib import admin
from .models import User, CompanyProfile, PayPalAccount

#  register the user and PaypalAccount model
admin.site.register(User)
admin.site.register(CompanyProfile)
admin.site.register(PayPalAccount)