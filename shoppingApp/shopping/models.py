from django.db import models

# Create your models here.

# Buraya Modellerimizi yüklüyoruz
# Ben bir deneme modeli yükleyeceğim


class DenemeProduct(models.Model):
    # burası bizim tablomuzun oldugu yer
    title = models.CharField(max_length = 200)
    price = models.CharField(max_length = 100)
    rating = models.CharField(max_length = 50)

    