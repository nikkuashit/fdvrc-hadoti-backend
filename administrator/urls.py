from django.urls import path, include
from rest_framework import routers
from .views import (CompanyProfileView, SocialLinkView,
                    CompanyProfileAdminView, SocialLinkAdminView)
router = routers.DefaultRouter()
# router.register('projects', ProjectView)
router.register('company-profile', CompanyProfileView)
router.register('company-profile-admin', CompanyProfileAdminView, basename='companyprofile-admin')
router.register('social-link', SocialLinkView)
router.register('social-link-admin', SocialLinkAdminView, basename='sociallink-admin')

urlpatterns = [
    path('', include(router.urls)),
    #  path('profilebydepartment/<str:slug>', CompanyProfileView.as_view()),

]
