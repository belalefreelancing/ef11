from django.db import models

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='BannerImage')
    http_link = models.URLField(max_length = 200, blank=True, null=True)
    

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='CategoryImage')

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ProductImage')
    price  = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name