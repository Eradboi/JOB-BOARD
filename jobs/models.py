from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from .code_gen import create_slug_code


# Create your models here.

# model for job upload
class Jobpost(models.Model):

    TYPE_CHOICES = (
        ('ON-SITE', 'ON-SITE'),
        ('REMOTE', 'REMOTE'),
        ('HYBRID', 'HYBRID')
    )
    CATEGORY_CHOICES = (
        ('FULL TIME', 'FULL TIME'),
        ('INTERNSHIP', 'INTERNSHIP'),
        ('CONTRACT', 'CONTRACT'),
    )
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=200, blank =True, null=True, choices=TYPE_CHOICES)
    category = models.TextField(null=True, blank=False, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=create_slug_code())

    class Meta:
        ordering = ["-created_at"]

    def get_detail(self):
        return reverse("jobs:job_detail", kwargs={
            'slug': self.slug,
            'title':self.title,
        })

    def add_bookmark(self):
        return reverse("jobs:add_bookmark", kwargs={
            'slug': self.slug,
        })

    def __str__(self):
        return f"{self.title}"

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="bookmarker",  on_delete=models.CASCADE)
    job = models.ForeignKey('Jobpost', on_delete=models.CASCADE)
