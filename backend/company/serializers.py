from rest_framework import serializers

from .models import CompanyProfile


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = [
            'company_name',
            'company_location',
            'company_website',
            'company_size',
            'company_logo',
        ]


class CompanyProfileLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = [
            'company_logo',
        ]

    def update(self, instance, validated_data):
        print('validated_data: ', validated_data)
        company_logo = validated_data.get('company_logo', None)
        if company_logo is not None:
            instance.company_logo = company_logo
            instance.save()
        return instance
