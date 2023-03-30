from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    title = models.CharField( max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE) # one other could have multiple posts that's why it's a foreign key
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title