from django.urls import path, include
from rest_framework import routers
from .views import (MenuView, MenuAdminView,
                    CorePageView, CorePagedminView, SectionView, SectionAdminView)
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('menu', MenuView)
router.register('menu-admin', MenuAdminView, basename='menu-admin')
router.register('core-page', CorePageView)
router.register('core-page-admin', CorePagedminView, basename='corepage-admin')
router.register('section', SectionView)
router.register('section-admin', SectionAdminView, basename='section-admin')

urlpatterns = [
    path('', include(router.urls)),
    #  path('profilebydepartment/<str:slug>', CompanyProfileView.as_view()),

]
