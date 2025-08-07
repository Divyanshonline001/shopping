from django.db import models

# Create your models here.

class Shops(models.Model):    ##STEP 2
    shop_name=models.CharField(max_length=200)
    content=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    shelf=models.CharField(max_length=200)
    expire_date=models.DateTimeField(auto_created=True)