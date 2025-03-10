from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  GroupItem = models.ForeignKey('ItemGroup', on_delete=models.CASCADE, blank=True, null=True)
  # priority = 

  def __str__(self):
    return self.title
  
class GroupItem(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name