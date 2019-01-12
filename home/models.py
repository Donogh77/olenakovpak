from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    text = models.TextField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now, blank=True,                                                 null=True)
    published_date = models.DateTimeField(default=timezone.now, blank=True,                                                 null=True)
    image = models.ImageField(upload_to='static/home', blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now
        self.save()
    
'''    def __str__(self):
        if self.text:
            return self.text
'''
'''
        if self.image:
            return self.image
Exception Type:	TypeError
Exception Value:	
__str__ returned non-string (type ImageFieldFile)
'''