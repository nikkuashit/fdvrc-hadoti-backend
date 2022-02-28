from django.db import models
import uuid
from django.db.models.base import Model
from slugify import slugify
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class ComponentType(models.Model):
    component_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.component_name


class Menu(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    on_footer = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(str(id))
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class CorePage(models.Model):
    slug = models.SlugField(unique=True)
    menu_id = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu')
    title = models.CharField(max_length=255, unique=True)
    sub_title = models.CharField(max_length=255, blank=True)
    content = RichTextField(blank=True, null=False)

    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(str(id))
        super(CorePage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Core Page"


class Section(models.Model):
    title = models.CharField(max_length=255, unique=True)
    position = models.IntegerField()
    content = RichTextField(blank=True, null=False)
    component_type = models.ForeignKey(
        ComponentType, to_field="component_name", on_delete=models.CASCADE, related_name='component_type')
    core_page = models.ForeignKey(
        CorePage, to_field="title", on_delete=models.CASCADE, related_name='core_page')

    def __str__(self):
        return (self.title)
