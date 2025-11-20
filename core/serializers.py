# from hadoti_backend.component.serializers import KnowAboutUsReadOnlySerializer, MediaFileReadOnlySerializer, ProductReadOnlySerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Menu, CorePage, Section, ComponentType)
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
    GlanceCreateSerializer,
    AnnouncementReadOnlySerializer,
    AnnouncementCreateSerializer,
    MediaFileReadOnlySerializer,
    MediaFileCreateSerializer,
    ComponentDataReadOnlySerializer
)
# Menu serializer

# CorePage  serializer


class SectionReadOnlySerializer(serializers.ModelSerializer):
    component_data = serializers.SerializerMethodField()
    component_type = serializers.CharField(source='component_type.component_name', read_only=True)
    core_page = serializers.CharField(source='core_page.title', read_only=True)

    class Meta:
        model = Section
        fields = ('position', 'component_type', 'title', 'content',
                  'core_page', 'id', 'component_data', 'media_file')

    def get_component_data(self, obj):
        """Get component data from all component tables based on component type"""
        # Import here to avoid circular imports
        from component.serializers import (
            ComponentDataReadOnlySerializer,
            CardMenuReadOnlySerializer,
            ProductReadOnlySerializer,
            KnowAboutUsReadOnlySerializer,
            LatestNewsReadOnlySerializer,
            FAQReadOnlySerializer,
            GlanceReadOnlySerializer,
            AnnouncementReadOnlySerializer,
            MediaFileReadOnlySerializer
        )

        component_type = obj.component_type.component_name

        # Map component types to their related names and serializers
        component_mapping = {
            'slider': ('component_data', ComponentDataReadOnlySerializer),
            'info_center': ('component_data', ComponentDataReadOnlySerializer),
            'center_card': ('card_section', CardMenuReadOnlySerializer),
            'slider_square': ('component_data', ComponentDataReadOnlySerializer),
            'left_card': ('card_section', CardMenuReadOnlySerializer),
            'left_to_right': ('component_data', ComponentDataReadOnlySerializer),
            'right_to_left': ('component_data', ComponentDataReadOnlySerializer),
            'slider_circle': ('component_data', ComponentDataReadOnlySerializer),
            'square_card_hover': ('card_section', CardMenuReadOnlySerializer),
            'team_member': ('component_data', ComponentDataReadOnlySerializer),
            'latest_news': ('news_section', LatestNewsReadOnlySerializer),
            'testimonial': ('component_data', ComponentDataReadOnlySerializer),
            'faq': ('faq_section', FAQReadOnlySerializer),
            'left_right_card': ('card_section', CardMenuReadOnlySerializer),
            'two_section': ('component_data', ComponentDataReadOnlySerializer),
            'download_card': ('component_data', ComponentDataReadOnlySerializer),
            'progress_number': ('glance_section', GlanceReadOnlySerializer),
            'chart': ('glance_section', GlanceReadOnlySerializer),
            'collapse': ('component_data', ComponentDataReadOnlySerializer),
            'product_enquiry': ('product_section', ProductReadOnlySerializer),
            'media': ('media_section', MediaFileReadOnlySerializer),
            'normal-card': ('card_section', CardMenuReadOnlySerializer),
            'contact': ('component_data', ComponentDataReadOnlySerializer),
            'bgimage-content': ('component_data', ComponentDataReadOnlySerializer),
            'position': ('component_data', ComponentDataReadOnlySerializer),
            'fileupload': ('component_data', ComponentDataReadOnlySerializer),
            'tender': ('component_data', ComponentDataReadOnlySerializer),
            'partnership': ('component_data', ComponentDataReadOnlySerializer)
        }

        if component_type in component_mapping:
            related_name, serializer_class = component_mapping[component_type]
            related_objects = getattr(obj, related_name).all()
            return serializer_class(related_objects, many=True).data

        # Fallback to component_data
        return ComponentDataReadOnlySerializer(obj.component_data.all(), many=True).data


class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['title', 'position', 'media_file', 'content', 'component_type', 'core_page']

    def create(self, validated_data):
        section = Section(**validated_data)
        section.save()
        return section

    def to_representation(self, instance):
        return SectionReadOnlySerializer(instance).data


class CorePageReadOnlySerializer(serializers.ModelSerializer):
    core_page = SectionReadOnlySerializer(source='sections', many=True, read_only=True)

    class Meta:
        model = CorePage
        fields = ('slug', 'menu_id', 'title',
                  'sub_title', 'content', 'core_page', 'id')


class CorePageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorePage
        fields = ['title', 'sub_title', 'content', 'menu_id']

    def create(self, validated_data):
        core_page = CorePage(**validated_data)
        core_page.save()
        return core_page


class MenuReadOnlySerializer(serializers.ModelSerializer):
    page = serializers.SerializerMethodField("get_core_page")

    class Meta:
        model = Menu
        fields = ('slug', 'title', 'link', 'page', 'on_footer', 'id')

    def get_core_page(self, obj):
        core_page = CorePage.objects.filter(menu_id=obj.id)
        data = json.loads(serial.serialize('json', core_page, fields=(
            'slug', 'title', 'sub_title', 'content', 'id')))
        return data


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'link', 'on_footer']

    def create(self, validated_data):
        menu = Menu(**validated_data)
        menu.save()
        return menu


class ComponentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentType
        fields = ['id', 'component_name']
