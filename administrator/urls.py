from django.urls import path, include
from rest_framework import routers
from .views import (CompanyProfileView, SocialLinkView)
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('company-profile', CompanyProfileView)
router.register('social-link', SocialLinkView)

urlpatterns = [
    path('', include(router.urls)),
    #  path('profilebydepartment/<str:slug>', CompanyProfileView.as_view()),

]
