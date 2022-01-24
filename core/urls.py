from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import (MenuView, MenuAdminView,
                    CorePageView, CorePagedminView)
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('menu', MenuView)
router.register('menu-admin', MenuAdminView)
router.register('core-page', CorePageView)
router.register('core-page-admin', CorePagedminView)

urlpatterns = [
    path('', include(router.urls)),
    #  path('profilebydepartment/<str:slug>', CompanyProfileView.as_view()),

]
