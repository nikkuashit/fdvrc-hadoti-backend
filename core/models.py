from django.db import models
import uuid
from slugify import slugify

# Create your models here.


class Menu(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)

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
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        id = uuid.uuid4()
        self.slug = slugify(str(id))
        super(CorePage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Core Page"
