"""hadoti_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="FDVRC Hadoti Backend API",
        default_version='v1',
        description="REST API for Singdev Mahila Kisan Utpadak Producer Company Limited - A comprehensive API for managing company profile, content pages, sections, and component data.",
        terms_of_service="https://singdevfpc.in/terms/",
        contact=openapi.Contact(email="customercare@singdevfpc.in"),
        license=openapi.License(name="Proprietary"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', include('accounts.urls')),
    path('administrator/', include('administrator.urls')),
    path('core/', include('core.urls')),
    path('component/', include('component.urls')),
    path('marketplace/', include('marketplace.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
