from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    todoUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todoUser', null=True, blank=False) 
    complete = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(blank=False)