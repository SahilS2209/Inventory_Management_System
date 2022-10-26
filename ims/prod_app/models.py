from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(default ='', max_length=30)
    email = models.EmailField()
    phone = models.CharField(default = '',max_length=10)
    desc = models.TextField(default ='')
    
    def __str__(self):
        return self.name + " - " + self.email
    
class Category(models.Model):
    category_name = models.CharField(max_length=100, null = False)
    
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    category_name = models.CharField(default = '', max_length=100)
    price = models.IntegerField(default=0)
    purchase_date = models.DateField()
    
    def __str__(self):
        return self.product_name