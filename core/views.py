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
from .models import (Menu, CorePage, Section)
from .serializers import (
    MenuReadOnlySerializer, MenuCreateSerializer, CorePageReadOnlySerializer, CorePageCreateSerializer, SectionReadOnlySerializer, SectionCreateSerializer)
from django_filters.rest_framework import DjangoFilterBackend


# Company Profile View


class MenuView(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    queryset = Menu.objects.all()
    # lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('on_footer',)

    serializer_class = MenuReadOnlySerializer
    serializer_action_classes = {
        'create': MenuCreateSerializer,
        'list': MenuReadOnlySerializer,
        'retrieve': MenuCreateSerializer
    }

    class Meta:
        model = Menu
        fields = '__all__'

# Company Profile View for admin


class MenuAdminView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    # lookup_field = 'slug'
    serializer_class = MenuReadOnlySerializer
    serializer_action_classes = {
        'create': MenuCreateSerializer,
        'list': MenuReadOnlySerializer,
        'retrieve': MenuCreateSerializer
    }

    class Meta:
        model = Menu
        fields = '__all__'


# Social Link View

class CorePageView(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    queryset = CorePage.objects.all()
    # lookup_field = 'slug'
    serializer_class = CorePageReadOnlySerializer
    serializer_action_classes = {
        'create': CorePageCreateSerializer,
        'list': CorePageReadOnlySerializer,
        'retrieve': CorePageCreateSerializer
    }

    class Meta:
        model = CorePage
        fields = '__all__'


class CorePagedminView(viewsets.ModelViewSet):
    queryset = CorePage.objects.all()
    # lookup_field = 'slug'
    serializer_class = CorePageReadOnlySerializer
    serializer_action_classes = {
        'create': CorePageCreateSerializer,
        'list': CorePageReadOnlySerializer,
        'retrieve': CorePageCreateSerializer
    }

    class Meta:
        model = CorePage
        fields = '__all__'


# Section page


class SectionView(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    queryset = Section.objects.all()
    # lookup_field = 'slug'
    serializer_class = SectionReadOnlySerializer
    serializer_action_classes = {
        'create': SectionCreateSerializer,
        'list': SectionReadOnlySerializer,
        'retrieve': SectionCreateSerializer
    }

    class Meta:
        model = Section
        fields = '__all__'


class SectionAdminView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    # lookup_field = 'slug'
    serializer_class = SectionReadOnlySerializer
    serializer_action_classes = {
        'create': SectionCreateSerializer,
        'list': SectionReadOnlySerializer,
        'retrieve': SectionCreateSerializer
    }

    class Meta:
        model = Section
        fields = '__all__'
