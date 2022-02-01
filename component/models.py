from abc import abstractclassmethod
from lib2to3.pytree import Base
from django.db import models
from django.db.models.expressions import Value

from core.models import (Section)
# Create your models here.


class BaseComponentModel(models.Model):

    title = models.CharField(max_length=255)
    media = models.FileField(null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now=True)
    position = models.IntegerField()
    on_landing = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True


class ComponentData(BaseComponentModel):

    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='component_data')
    is_active = models.BooleanField(default=True)
    value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Component Data"


class CardMenu(BaseComponentModel):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='card_section')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Card Menu"


class Product(BaseComponentModel):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='product_section')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product"


class KnowAboutUs(BaseComponentModel):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='know_section')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Know About Us"


class LatestNews(BaseComponentModel):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='news_section')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Latest News"


class FAQ(BaseComponentModel):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='faq_section')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "FAQ"


class Glance(models.Model):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='glance_section')
    title = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Glance"


class Announcement(BaseComponentModel):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='announcement_section')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Announcement"


class MediaFile(BaseComponentModel):
    section_id = models.ForeignKey(
        Section, on_delete=models.CASCADE,  related_name='media_section')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Media"
