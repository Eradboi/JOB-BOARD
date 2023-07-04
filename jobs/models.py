from django.db import models



# Create your models here.
# model for job upload
class Upload(models.Model):

    TYPE_CHOICES = (
        ('ON-SITE', 'ON-SITE'),
        ('REMOTE', 'REMOTE'),
        ('HYBRID', 'HYBRID')
    )
    DURATION_CHOICES = (
        ('Less than a week', 'Less than a week'),
        ('1 to 4 weeks', '1 to 4 weeks'),
        ('1 to 3 months', '1 to 3 months'),
        ('More than 3 months', 'More than 3 months'),
    )

    Description = models.TextField()
    Title = models.CharField(max_length=50)
    Type = models.CharField(max_length=200, blank =True, null=True, choices=TYPE_CHOICES)
    Duration = models.TextField(null=True, blank=False, choices=DURATION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
