from django.urls import path, include
from rest_framework import routers
from .views import (
    ComponentDataView, CardMenuView, ProductView, KnowAboutUsView,
    LatestNewsView, FAQView, GlanceView, AnnouncementView, MediaFileView
)

router = routers.DefaultRouter()
router.register('component-data', ComponentDataView)
router.register('card-menu', CardMenuView)
router.register('products', ProductView)
router.register('know-about-us', KnowAboutUsView)
router.register('latest-news', LatestNewsView)
router.register('faq', FAQView)
router.register('glance', GlanceView)
router.register('announcements', AnnouncementView)
router.register('media-files', MediaFileView)

urlpatterns = [
    path('', include(router.urls)),
]