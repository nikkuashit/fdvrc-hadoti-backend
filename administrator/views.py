from rest_framework import viewsets
import json
import requests
from django.http import Http404, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status
from django.contrib.auth.models import User
from hadoti_backend.permissions import IsAdminOrStaffOrReadOnly
from .models import (CompanyProfile, SocialLink)
from .serializers import (
    CompanyProfileReadOnlySerializer, CompanyProfileCreateSerializer, SocialLinkReadOnlySerializer, SocialLinkCreateSerializer)

# Company Profile View


class CompanyProfileView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = CompanyProfile.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CompanyProfileCreateSerializer
        return CompanyProfileReadOnlySerializer

# Social Link View

class SocialLinkView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = SocialLink.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SocialLinkCreateSerializer
        return SocialLinkReadOnlySerializer


