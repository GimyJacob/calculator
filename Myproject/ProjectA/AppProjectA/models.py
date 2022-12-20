from django.db import models

# Create your models here.
class fashion(models.Model):
    fashion_name=models.CharField(max_length=200)
    fashion_loc=models.CharField(max_length=100)
    fashion_img=models.ImageField(upload_to='pics')

class Fash(models.Model):
    fash_name=models.CharField(max_length=200)
    fash_content=models.CharField(max_length=300)
    fash_img=models.ImageField(upload_to='pics')
class Fash2(models.Model):
    fash2_img = models.ImageField(upload_to='pics')

def __str__(self):
    return self.name