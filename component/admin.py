from django.contrib import admin
from .models import (CardMenu, Product, KnowAboutUs,
                     LatestNews, FAQ, Glance, Announcement, MediaFile)
# Register your models here.
admin.site.register(CardMenu)
admin.site.register(Product)
admin.site.register(KnowAboutUs)
admin.site.register(LatestNews)
admin.site.register(FAQ)
admin.site.register(Glance)
admin.site.register(Announcement)
admin.site.register(MediaFile)
