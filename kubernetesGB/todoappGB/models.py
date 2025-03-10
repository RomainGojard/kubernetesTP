from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    UserItem = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # Utiliser le modèle User de Django
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Priority(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()