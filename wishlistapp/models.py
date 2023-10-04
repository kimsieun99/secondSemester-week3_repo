from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title
    
    
