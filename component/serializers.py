from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (CardMenu,
                     Product,
                     KnowAboutUs,
                     LatestNews,
                     FAQ,
                     Glance,
                     Announcement,
                     MediaFile, ComponentData)
from django.core import serializers as serial
import json
# ComponentData


class ComponentDataReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = ComponentData
        fields = '__all__'


class ComponentDataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentData

    def create(self, validated_data):
        component_data = ComponentData(**validated_data)
        component_data.save()
        return component_data

# CardMenu


class CardMenuReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = CardMenu
        fields = '__all__'


class CardMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardMenu

    def create(self, validated_data):
        card_menu = CardMenu(**validated_data)
        card_menu.save()
        return card_menu

# Product


class ProductReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

# KnowAboutUs


class KnowAboutUsReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = KnowAboutUs
        fields = '__all__'


class KnowAboutUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowAboutUs

    def create(self, validated_data):
        know_abou_us = KnowAboutUs(**validated_data)
        know_abou_us.save()
        return know_abou_us

# LatestNews


class LatestNewsReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = LatestNews
        fields = '__all__'


class LatestNewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNews

    def create(self, validated_data):
        latest_news = LatestNews(**validated_data)
        latest_news.save()
        return latest_news
# FAQ


class FAQReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ('slug', 'menu_id', 'title',
                  'sub_title', 'content', 'core_page')


class FAQCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ

    def create(self, validated_data):
        faq = FAQ(**validated_data)
        faq.save()
        return faq
# Glance


class GlanceReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Glance
        fields = '__all__'


class GlancereateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glance

    def create(self, validated_data):
        glance = Glance(**validated_data)
        glance.save()
        return glance

# Announcement


class AnnouncementReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = '__all__'


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement

    def create(self, validated_data):
        announcement = Announcement(**validated_data)
        announcement.save()
        return announcement

# MediaFile


class MediaFileReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaFile
        fields = '__all__'


class MediaFileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile

    def create(self, validated_data):
        media_file = MediaFile(**validated_data)
        media_file.save()
        return media_file
