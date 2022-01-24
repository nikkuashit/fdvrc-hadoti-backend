from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import (CompanyProfileView, SocialLinkView,
                    CompanyProfileAdminView, SocialLinkAdminView)
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('company-profile', CompanyProfileView)
router.register('company-profile-admin', CompanyProfileAdminView)
router.register('social-link', SocialLinkView)
router.register('social-link-admin', SocialLinkAdminView)

urlpatterns = [
    path('', include(router.urls)),
    #  path('profilebydepartment/<str:slug>', CompanyProfileView.as_view()),

]
