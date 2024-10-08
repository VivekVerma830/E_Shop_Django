from typing import Iterable
from django.db import models
from django.utils import timezone

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)

class Brand(models.Model):
    name = models.CharField(max_length=200)

class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1000 TO 10000' ,'1000 TO 10000'),
        ('10000 TO 20000' ,'10000 TO 20000'),
        ('20000 TO 30000' ,'20000 TO 30000'),
        ('30000 TO 40000' ,'30000 TO 40000'),
        ('40000 TO 50000' ,'40000 TO 50000'),
    )
    price = models.CharField(choices=FILTER_PRICE , max_length=60)

class Product(models.Model):
    CONDITION = (('New','New'),('Old','Old'))
    STOCK = ('IN STOCK','IN STOCK'),('OUT OF STOCK', 'OUT OF STOCK')
    STATUS =('Public','Public'),('Draft','Draft')

    unique_id = models.CharField(unique=True, max_length=200 ,null=True, blank=True)
    image = models.ImageField(upload_to='Product_image/img') 
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = models.TextField()
    description = models.TextField() 
    stock = models.TextField(choices=STOCK , max_length=200)
    status = models.TextField(choices=STATUS,max_length=200)
    created_date = models.DateField(default=timezone.now)

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)

    def save(self, args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str (self.id)
        return super().save(args, **kwargs)
    


