from django.contrib import admin

# Register your models here.
from .models import (Menu, CorePage, Section, ComponentType)
# Register your models here.
admin.site.register(Menu)
admin.site.register(CorePage)
admin.site.register(Section)
admin.site.register(ComponentType)
