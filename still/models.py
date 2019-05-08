from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    text = models.TextField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)
    published_date = models.DateField(default=timezone.now, blank=True, null=True)
    image = models.ImageField(upload_to='static/still')
    
    def publish(self):
        self.published_date = timezone.now
        self.save()