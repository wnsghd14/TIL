from django.db import models
from django.forms import CharField

# Create your models here.
class Review(models.Model):
  title = models.CharField(max_length=80,null=True)
  content = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True)

