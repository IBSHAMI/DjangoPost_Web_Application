from rest_framework import serializers

from .models import CompanyProfile


class CompanyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = [
            'company_name',
            'company_description',
            'company_location',
            'company_website',
            'company_size',
            'company_logo',
        ]
