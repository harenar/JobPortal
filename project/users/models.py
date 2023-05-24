from django.db import models

# Create your models here.

class User_register(models.Model):
    User_name = models.CharField( max_length=50)
    User_email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=50)
    Con_password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.User_name
    
    
