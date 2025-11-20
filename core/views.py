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
from hadoti_backend.permissions import IsAdminOrStaffOrReadOnly, IsAdminOrStaffOnly
from .models import (Menu, CorePage, Section, ComponentType)
from .serializers import (
    MenuReadOnlySerializer, MenuCreateSerializer, CorePageReadOnlySerializer, CorePageCreateSerializer, SectionReadOnlySerializer, SectionCreateSerializer, ComponentTypeSerializer)
from django_filters.rest_framework import DjangoFilterBackend


# Company Profile View


class MenuView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = Menu.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('on_footer',)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MenuCreateSerializer
        return MenuReadOnlySerializer

# Core Page View

class CorePageView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = CorePage.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CorePageCreateSerializer
        return CorePageReadOnlySerializer


# Section View


class SectionView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = Section.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SectionCreateSerializer
        return SectionReadOnlySerializer


# ComponentType View

class ComponentTypeView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrStaffOrReadOnly]
    queryset = ComponentType.objects.all()
    serializer_class = ComponentTypeSerializer


