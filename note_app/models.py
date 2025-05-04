from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    isPublished = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title