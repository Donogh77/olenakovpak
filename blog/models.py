from django.db import models
from django.utils import timezone
from olenakovpak.settings import STATIC_ROOT

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(default=timezone.now, blank=True,                                                 null=True)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=STATIC_ROOT, blank=True, null=True)
    # Add functionality to add videos
    
    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return self.title