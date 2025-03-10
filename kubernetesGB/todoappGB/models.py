from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  
class ItemGroup(models.Model):
  name = models.CharField(max_length=200)
  items = models.ManyToManyField(TodoItem, blank=True)

  def __str__(self):
    return self.name