from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (CompanyProfile, SocialLink)

# Company profile serializer


class CompanyProfileReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


class CompanyProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile

    def create(self, validated_data):
        company_profile = CompanyProfile(**validated_data)
        company_profile.save()
        return company_profile

 # Social link serializer


class SocialLinkReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class SocialLinkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink

    def create(self, validated_data):
        social_link = SocialLink(**validated_data)
        social_link.save()
        return social_link
