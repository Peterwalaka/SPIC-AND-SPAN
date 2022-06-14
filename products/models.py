from django.db import models
from django.shortcuts import reverse
from PIL import Image
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    IMG_DIMENSION = 540

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='products/')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        with Image.open(self.thumbnail.path) as img:
            if img.height > self.IMG_DIMENSION or img.width > self.IMG_DIMENSION:
                img.thumbnail((self.IMG_DIMENSION, self.IMG_DIMENSION))
                img.save(self.thumbnail.path)

    def get_product_url(self):
        return reverse("products:product-detail", kwargs={
            'pk': self.pk
        })
        
class Sell(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='sells/')
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    price =models.FloatField()
    negotiable = models.BooleanField()
    phone_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
           
    class Meta:
        ordering = ['pk']

        def __str__(self):
            return self.name
"""      
        def get_absolute_url(self):       
              return reverse('sell_detail', args=[str(self.id)]) 
"""                   
"""
        def save(self):
            super().save()

            with Image.open(self.thumbnail.path) as img:
                if img.height > self.IMG_DIMENSION or img.width > self.IMG_DIMENSION:
                    img.thumbnail((self.IMG_DIMENSION, self.IMG_DIMENSION))
                    img.save(self.thumbnail.path)

            def get_sell_url(self):
             return reverse("sells:sell-detail", kwargs={
            'pk': self.pk
        })
   
"""         