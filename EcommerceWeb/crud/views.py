from django.shortcuts import render, redirect
import pymongo
from ecommerce.models import MatchProducts

# Create your views here.


def addProduct(request):

    if request.method == "POST":
        print("pOSTA GİRDİM")
        marka = request.POST['marka']
        modelAdi = request.POST['modelAdi']
        modelNo = request.POST['modelNo']
        isletimSistemi = request.POST['isletimSistemi']
        islemciTipi = request.POST['islemciTipi']
        islemciNesli = request.POST['islemciNesli']
        ram = request.POST['ram']
        diskBoyutu = request.POST['diskBoyutu']
        diskTuru = request.POST['diskTuru']
        ekranBoyu = request.POST['ekranBoyu']
        puani = request.POST['puani']
        fiyat = request.POST['fiyat']
        prodLink = request.POST['prodLink']
        prodImageLink = request.POST['prodImageLink']
        prodTitle = request.POST['prodTitle']
        site = request.POST['site']
        id = request.POST['id']

        print(marka)
        # baglanma islemi
        myClient = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']


        myCollection = mydb['ecommerce_matchproducts']
        base = {}
        base['modelNo']= modelNo
        
        tempProduct = myCollection.find(base)
        tempProduct = list(tempProduct)
        
        if len(tempProduct) == 0 :
            base = {}

            base['marka']= marka
            base['modelAdi']= modelAdi
            base['modelNo']= modelNo
            base['isletimSistemi']= isletimSistemi
            base['islemciTipi']= islemciTipi
            base['islemciNesli']= islemciNesli
            base['ram']= ram
            base['diskBoyutu']= diskBoyutu
            base['diskTuru']= diskTuru
            base['ekranBoyu']= ekranBoyu
            base['puani']= puani
            base['fiyat']= float(fiyat)
            base['prodLink']= prodLink
            base['prodImageLink']= prodImageLink
            base['prodTitle']= prodTitle
            base['site']= site
            base['id']= int(id)

            myCollection.insert_one(base)
            print("Siteye Eklendi")

            # veri tabanına kaydettim

            # sen buray tekrardan veri tabanından kayıtlı verileri kendi sitene her zmanki gibi cek

            return redirect('home')

        else:
            print("Bu veri Sitemizde Zaten var")
            return redirect('home')

        
    


    return render(request, "crud/add.html")


def updateProduct(request, id):

    selectedProd = MatchProducts.objects.get(id=id)

    prod={
        "selectedProd": selectedProd
    }



    if request.method == "POST":
        print("pOSTA GİRDİM")
        marka = request.POST['marka']
        modelAdi = request.POST['modelAdi']
        modelNo = request.POST['modelNo']
        isletimSistemi = request.POST['isletimSistemi']
        islemciTipi = request.POST['islemciTipi']
        islemciNesli = request.POST['islemciNesli']
        ram = request.POST['ram']
        diskBoyutu = request.POST['diskBoyutu']
        diskTuru = request.POST['diskTuru']
        ekranBoyu = request.POST['ekranBoyu']
        puani = request.POST['puani']
        fiyat = request.POST['fiyat']
        prodLink = request.POST['prodLink']
        prodImageLink = request.POST['prodImageLink']
        prodTitle = request.POST['prodTitle']
        site = request.POST['site']
        id = request.POST['id']

        print(marka)
        # baglanma islemi
        myClient = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']


        myCollection = mydb['ecommerce_matchproducts']
        base = {}
        base['modelNo']= modelNo
        
        tempProduct = myCollection.find(base)
        tempProduct = list(tempProduct)
        
        if len(tempProduct) != 0 :
            
            kalıp2 = {}

            kalıp2['modelNo']=modelNo
            toplu = {}
            toplu['marka']= marka
            toplu['modelAdi']= modelAdi
            toplu['modelNo']= modelNo
            toplu['isletimSistemi']= isletimSistemi
            toplu['islemciTipi']= islemciTipi
            toplu['islemciNesli']= islemciNesli
            toplu['ram']= ram
            toplu['diskBoyutu']= diskBoyutu
            toplu['diskTuru']= diskTuru
            toplu['ekranBoyu']= ekranBoyu
            toplu['puani']= puani
            toplu['fiyat']= float(fiyat)
            toplu['prodLink']= prodLink
            toplu['prodImageLink']= prodImageLink
            toplu['prodTitle']= prodTitle
            toplu['site']= site
            toplu['id']= int(id)

            kalıp = {}

            kalıp['$set'] = toplu

            
            
            
            myCollection.update_one(kalıp2, kalıp)

            print("Urun  Guncelledi")

            # veri tabanına kaydettim

            # sen buray tekrardan veri tabanından kayıtlı verileri kendi sitene her zmanki gibi cek

            return redirect('home')

        else:
            print("Bu veri Sitemizde Bulunmuyor Güncelleyemezsiniz")
            return redirect('home')

        
    


    


    return render(request, "crud/update.html", prod)

def deleteProduct(request):

    if request.method == "POST":
        modelNo = request.POST['modelNo']

        # baglanma islemi
        myClient = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']


        myCollection = mydb['ecommerce_matchproducts']

        myCollection.delete_one({'modelNo':modelNo})

        print('Isleminiz Gerceklesmistir')

        return redirect('home')

    return render(request, "crud/delete.html")