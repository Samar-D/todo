from django.db import models

# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    year = models.DateField(max_length=4)
    date = models.DateField(auto_now_add=True)