import uuid
from django.db import models
from django.conf import settings
from datetime import datetime

User=settings.AUTH_USER_MODEL

class Category(models.Model):
    name=models.CharField(max_length=70)


    def __str__(self):
        return self.name

class Items(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    Item=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=50)
    slug=models.SlugField()
    status=models.CharField(max_length=500)
    date = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.Item
