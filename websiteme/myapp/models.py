# models.py
from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30,blank=True)
    phonenumber=models.IntegerField(max_length=30,blank=True)
    address_line=models.CharField(max_length=30,blank=True)
    postcode=models.CharField(max_length=30,blank=True)
    email=models.EmailField(max_length=30,blank=True)
    country=models.CharField(max_length=30,blank=True)
    state_region=models.CharField(max_length=30,blank=True)
    # profilepic = models.ImageField(upload_to='D:\loginweb\websiteme\static\profilepic/proof.png', default='D:\loginweb\websiteme\static\profilepic\default.png')
    


    

    def __str__(self):
        return self.user.username
class House(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_for_sale = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title