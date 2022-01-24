from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Menu, CorePage, Section)

# Menu serializer

# CorePage  serializer


class SectionReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('position', 'component_type', 'core_page')


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
                  'sub_title', 'content', 'core_page')


class CorePageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorePage

    def create(self, validated_data):
        core_page = CorePage(**validated_data)
        core_page.save()
        return core_page


class MenuReadOnlySerializer(serializers.ModelSerializer):
    menu = CorePageReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('slug', 'title', 'link', 'menu')


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu

    def create(self, validated_data):
        menu = Menu(**validated_data)
        menu.save()
        return menu
