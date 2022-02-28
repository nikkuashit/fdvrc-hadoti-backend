from django.db import models


class CompanyProfile(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField()
    sub_title = models.CharField(max_length=255, blank=True)
    sub_image = models.ImageField(blank=True)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country_code = models.CharField(max_length=5, blank=True)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, blank=True)
    footer_icon = models.ImageField(blank=True)
    footer_sub_image = models.ImageField(blank=True)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Company Profile"


class SocialLink(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField()
    url = models.URLField()
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Social Link"
