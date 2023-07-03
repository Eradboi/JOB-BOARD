from django.db import models



# Create your models here.
# model for job upload
class Upload(models.Model):

    Description = models.TextField()
    Title = models.CharField(max_length=50)
    Onsite = models.BooleanField(null=True, blank=False)
    Duration = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
