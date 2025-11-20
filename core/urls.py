from django.urls import path, include
from rest_framework import routers
from .views import (MenuView, CorePageView, SectionView, ComponentTypeView)
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('menu', MenuView)
router.register('core-page', CorePageView)
router.register('section', SectionView)
router.register('componenttype', ComponentTypeView)

urlpatterns = [
    path('', include(router.urls)),
    #  path('profilebydepartment/<str:slug>', CompanyProfileView.as_view()),

]
