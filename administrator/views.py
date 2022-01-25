from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
import requests
from django.http import Http404, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status
from django.contrib.auth.models import User
from .models import (CompanyProfile, SocialLink)
from .serializers import (
    CompanyProfileReadOnlySerializer, CompanyProfileCreateSerializer, SocialLinkReadOnlySerializer, SocialLinkCreateSerializer)

# Company Profile View


class CompanyProfileView(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    queryset = CompanyProfile.objects.all()
    # lookup_field = 'slug'
    serializer_class = CompanyProfileReadOnlySerializer
    serializer_action_classes = {
        'create': CompanyProfileCreateSerializer,
        'list': CompanyProfileReadOnlySerializer,
        'retrieve': CompanyProfileCreateSerializer
    }

    class Meta:
        model = CompanyProfile
        fields = '__all__'

# Company Profile View for admin


class CompanyProfileAdminView(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    # lookup_field = 'slug'
    serializer_class = CompanyProfileReadOnlySerializer
    serializer_action_classes = {
        'create': CompanyProfileCreateSerializer,
        'list': CompanyProfileReadOnlySerializer,
        'retrieve': CompanyProfileCreateSerializer
    }

    class Meta:
        model = CompanyProfile
        fields = '__all__'


# Social Link View

class SocialLinkView(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    queryset = SocialLink.objects.all()
    # lookup_field = 'slug'
    serializer_class = SocialLinkReadOnlySerializer
    serializer_action_classes = {
        'create': SocialLinkCreateSerializer,
        'list': SocialLinkReadOnlySerializer,
        'retrieve': SocialLinkCreateSerializer
    }

    class Meta:
        model = SocialLink
        fields = '__all__'


# Social Admin View

class SocialLinkAdminView(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    # lookup_field = 'slug'
    serializer_class = SocialLinkReadOnlySerializer
    serializer_action_classes = {
        'create': SocialLinkCreateSerializer,
        'list': SocialLinkReadOnlySerializer,
        'retrieve': SocialLinkCreateSerializer
    }

    class Meta:
        model = SocialLink
        fields = '__all__'
