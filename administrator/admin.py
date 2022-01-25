from django.contrib import admin
from .models import (CompanyProfile, SocialLink)
# Register your models here.
admin.site.register(CompanyProfile)
admin.site.register(SocialLink)