from rest_framework import viewsets
from hadoti_backend.permissions import IsAdminOrStaffOrReadOnly
from .models import (
    ComponentData, CardMenu, Product, KnowAboutUs, LatestNews,
    FAQ, Glance, Announcement, MediaFile
)
from .serializers import (
    ComponentDataReadOnlySerializer, ComponentDataCreateSerializer,
    CardMenuReadOnlySerializer, CardMenuCreateSerializer,
    ProductReadOnlySerializer, ProductCreateSerializer,
    KnowAboutUsReadOnlySerializer, KnowAboutUsCreateSerializer,
    LatestNewsReadOnlySerializer, LatestNewsCreateSerializer,
    FAQReadOnlySerializer, FAQCreateSerializer,
    GlanceReadOnlySerializer, GlanceCreateSerializer,
    AnnouncementReadOnlySerializer, AnnouncementCreateSerializer,
    MediaFileReadOnlySerializer, MediaFileCreateSerializer
)


# Permission class now imported from hadoti_backend.permissions


class ComponentDataView(viewsets.ModelViewSet):
    queryset = ComponentData.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ComponentDataCreateSerializer
        return ComponentDataReadOnlySerializer


class CardMenuView(viewsets.ModelViewSet):
    queryset = CardMenu.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CardMenuCreateSerializer
        return CardMenuReadOnlySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductCreateSerializer
        return ProductReadOnlySerializer


class KnowAboutUsView(viewsets.ModelViewSet):
    queryset = KnowAboutUs.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return KnowAboutUsCreateSerializer
        return KnowAboutUsReadOnlySerializer


class LatestNewsView(viewsets.ModelViewSet):
    queryset = LatestNews.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LatestNewsCreateSerializer
        return LatestNewsReadOnlySerializer


class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return FAQCreateSerializer
        return FAQReadOnlySerializer


class GlanceView(viewsets.ModelViewSet):
    queryset = Glance.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return GlanceCreateSerializer
        return GlanceReadOnlySerializer


class AnnouncementView(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AnnouncementCreateSerializer
        return AnnouncementReadOnlySerializer


class MediaFileView(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    permission_classes = [IsAdminOrStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MediaFileCreateSerializer
        return MediaFileReadOnlySerializer