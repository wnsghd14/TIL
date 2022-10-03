from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date
import datetime
# Create your models here.

class Todo(models.Model):
  name = models.CharField(max_length=10)
  content = models.CharField(max_length=80)
  completed = models.BooleanField(default=False)
  priority = models.IntegerField(default=3)
  created_at = models.DateField(auto_now_add=True)
  deadline = models.DateField(null=True)
  