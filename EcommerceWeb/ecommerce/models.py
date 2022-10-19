from django.db import models

class Prods(models.Model):
    # burası bizim tablomuzun oldugu yer
    marka = models.CharField(max_length = 200)
    modelAdi = models.CharField(max_length = 100)
    modelNo = models.CharField(max_length = 50)
    isletimSistemi = models.CharField(max_length = 100)
    islemciTipi = models.CharField(max_length = 100)
    islemciNesli = models.CharField(max_length = 100)
    ram = models.CharField(max_length = 100)
    diskBoyutu  = models.CharField(max_length = 100)
    diskTuru = models.CharField(max_length = 100)
    ekranBoyu = models.CharField(max_length = 100)
    puani = models.CharField(max_length = 100)
    fiyat = models.CharField(max_length = 100)
    site = models.CharField(max_length = 30) 
    prodLink=models.CharField(max_length = 200) 
    imageLink=models.CharField(max_length = 200) 
    prodTitle=models.CharField(max_length = 200) 
    
    def __str__(self):
        
        return f"{self.prodTitle}"


