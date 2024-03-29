from PIL import Image
from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

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
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

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
