from django.db import models

# Create your models here.

# Buraya Modellerimizi yüklüyoruz
# Ben bir deneme modeli yükleyeceğim


"""

'marka':marka,+
'modelAdi':model_adi, +
'modelNo':model_no, +
'isletimSistemi':isletimsistemi,+
'islemciTipi':islemci_tipi,+
'islemciNesli':islemcinesli,+
'ram':ram,+
'diskBoyutu':kapasite,+
'diskTuru':disk_tipi,+
'ekranBoyu':ekran_boyutu,+
'puani':puani,+
'fiyat':fiyat,+
'prodLink':url,+
'imageLink':imageLink,+
'prodTitle':prodTitle,+
'site':site+

"""

class Products(models.Model):
    # burası bizim tablomuzun oldugu yer
    marka = models.CharField(max_length = 50)
    modelAdi = models.CharField(max_length = 50)
    modelNo = models.CharField(max_length = 50)
    isletimSistemi = models.CharField(max_length = 50)
    islemciTipi = models.CharField(max_length = 50)
    islemciNesli = models.CharField(max_length = 50)
    ram = models.CharField(max_length = 50)
    diskBoyutu = models.CharField(max_length = 50)
    diskTuru = models.CharField(max_length = 50)
    ekranBoyu = models.CharField(max_length = 50)
    puani = models.CharField(max_length = 5)
    fiyat = models.DecimalField(max_digits=8, decimal_places=2)
    prodLink = models.CharField(max_length = 300)
    imageLink = models.CharField(max_length = 300)
    prodTitle = models.CharField(max_length = 300)
    site = models.CharField(max_length = 50)
    matchNo=models.IntegerField(default=None)

class MatchProducts(models.Model):
    # burası bizim tablomuzun oldugu yer
    marka = models.CharField(max_length = 50)
    modelAdi = models.CharField(max_length = 50)
    modelNo = models.CharField(max_length = 50)
    isletimSistemi = models.CharField(max_length = 50)
    islemciTipi = models.CharField(max_length = 50)
    islemciNesli = models.CharField(max_length = 50)
    ram = models.CharField(max_length = 50)
    diskBoyutu = models.CharField(max_length = 50)
    diskTuru = models.CharField(max_length = 50)
    ekranBoyu = models.CharField(max_length = 50)
    puani = models.CharField(max_length = 5)
    fiyat = models.DecimalField(max_digits=8, decimal_places=2)
    prodLink = models.CharField(max_length = 300)
    imageLink = models.CharField(max_length = 300)
    prodTitle = models.CharField(max_length = 300)
    site = models.CharField(max_length = 50)
    matchNo=models.IntegerField()


    

    