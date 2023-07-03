from django.db import models



# Create your models here.
# model for job upload
class Upload(models.Model):

    TYPE_CHOICES = (
        ('ON-SITE', 'ON-SITE'),
        ('REMOTE', 'REMOTE'),
        ('HYBRID', 'HYBRID')
    )

    Description = models.TextField()
    Title = models.CharField(max_length=50)
    Type = models.CharField(max_length=200, blank =True, null=True, choices=TYPE_CHOICES)
    Duration = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
