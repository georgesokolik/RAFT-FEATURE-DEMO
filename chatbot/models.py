from django.db import models

# Create your models here.

class Review(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)