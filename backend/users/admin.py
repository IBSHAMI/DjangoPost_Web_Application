from django.contrib import admin
from .models import User, EmployeeProfile, CompanyProfile, PayPalAccount

#  register the user and PaypalAccount model
admin.site.register(User)
admin.site.register(EmployeeProfile)
admin.site.register(CompanyProfile)
admin.site.register(PayPalAccount)