from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='properties/')
    listed_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    investment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} invested in {self.property.name}"

