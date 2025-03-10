from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  #group = models.CharField(blank=True)
  UserItem = models.ForeignKey('UserItem', on_delete=models.CASCADE, blank=True, null=True)
  priority = models.ForeignKey('Priority', on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.title

class UserItem(models.Model):
  name = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)

  def __str__(self):
    return self.name

class Priority(models.Model):
  name = models.CharField(max_length=200)
  value = models.IntegerField()