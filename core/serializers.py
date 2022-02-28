# from hadoti_backend.component.serializers import KnowAboutUsReadOnlySerializer, MediaFileReadOnlySerializer, ProductReadOnlySerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Menu, CorePage, Section)
from django.core import serializers as serial
import json

from component.serializers import (
    CardMenuReadOnlySerializer,
    CardMenuCreateSerializer,
    ProductReadOnlySerializer,
    ProductCreateSerializer,
    KnowAboutUsReadOnlySerializer,
    KnowAboutUsCreateSerializer,
    LatestNewsReadOnlySerializer,
    LatestNewsCreateSerializer,
    FAQReadOnlySerializer,
    FAQCreateSerializer,
    GlanceReadOnlySerializer,
    GlancereateSerializer,
    AnnouncementReadOnlySerializer,
    AnnouncementCreateSerializer,
    MediaFileReadOnlySerializer,
    MediaFileCreateSerializer,
    ComponentDataReadOnlySerializer
)
# Menu serializer

# CorePage  serializer


class SectionReadOnlySerializer(serializers.ModelSerializer):
    component_data = ComponentDataReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ('position', 'component_type', 'title', 'content',
                  'core_page', 'id', 'component_data')


class SectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section

    def create(self, validated_data):
        section = Section(**validated_data)
        section.save()
        return section


class CorePageReadOnlySerializer(serializers.ModelSerializer):
    core_page = SectionReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = CorePage
        fields = ('slug', 'menu_id', 'title',
                  'sub_title', 'content', 'core_page', 'id')


class CorePageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorePage

    def create(self, validated_data):
        core_page = CorePage(**validated_data)
        core_page.save()
        return core_page


class MenuReadOnlySerializer(serializers.ModelSerializer):
    page = serializers.SerializerMethodField("get_core_page")

    class Meta:
        model = Menu
        fields = ('slug', 'title', 'link', 'menu', 'page', 'on_footer', 'id')

    def get_core_page(self, obj):
        core_page = CorePage.objects.filter(menu_id=obj.id)
        data = json.loads(serial.serialize('json', core_page, fields=(
            'slug', 'title', 'sub_title', 'content', 'id')))
        return data


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu

    def create(self, validated_data):
        menu = Menu(**validated_data)
        menu.save()
        return menu
