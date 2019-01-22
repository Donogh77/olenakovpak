from django.db import models

# Create your models here.

class Submit_form(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    message = models.TextField()
    
    def publish(self):
        self.save()
