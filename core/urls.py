from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import (MenuView, MenuAdminView,
                    CorePageView, CorePagedminView, SectionView, SectionAdminView)
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('menu', MenuView)
router.register('menu-admin', MenuAdminView)
router.register('core-page', CorePageView)
router.register('core-page-admin', CorePagedminView)
router.register('section', SectionView)
router.register('section-admin', SectionAdminView)

urlpatterns = [
    path('', include(router.urls)),
    #  path('profilebydepartment/<str:slug>', CompanyProfileView.as_view()),

]
