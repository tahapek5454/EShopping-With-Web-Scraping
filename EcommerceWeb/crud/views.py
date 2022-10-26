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
        isletimSistemi = shapeIsletimSistemi(request.POST['isletimSistemi'])
        islemciTipi = request.POST['islemciTipi']
        islemciNesli = request.POST['islemciNesli']
        ram = request.POST['ram']
        diskBoyutu = request.POST['diskBoyutu']
        diskTuru = request.POST['diskTuru']
        ekranBoyu = shapeEkranBoyutu(request.POST['ekranBoyu'])
        puani = request.POST['puani']
        fiyat = shapeFiyat(request.POST['fiyat'])
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

def shapeFiyat(self, item):
        
        if item.find('T') !=-1 :
            item = item[:item.find('T')].strip()

        
        if item.find('.') != -1 :
            item = item.replace('.','')
         
        
        if item.find(',') != -1:
            item = item.replace(',','.')
         

        # finish cleaning

        # str to float

        item = float(item)
        return item
    
def shapeEkranBoyutu(self, item):

    if item.find('"') != -1:
        item = item[:item.find('"')].strip()
    
    elif item.find('i') != -1:
        item = item[:item.find('i')].strip()

    if item.find('.') != -1:
        item = item.replace('.',',')
    
    return item

def shapeIsletimSistemi(self, item):

    if item.find('Free') != -1:
        item = 'Freedos'
    if item.find('Yok')!=-1:
        item='Freedos'
    return item

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
        myClient2 = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')
        # database e gimre
        mydb = myClient['WebScraping']
        my_db2 = myClient2['WebScraping']

        myCollection = mydb['ecommerce_matchproducts']
        myCollection2 = my_db2['shopping_matchproducts']
        base = {}
        base['modelNo']= modelNo
        
        tempProduct = myCollection.find(base)
        tempProduct2 = myCollection2.find(base)
        tempProduct = list(tempProduct)
        tempProduct2 = list(tempProduct2)
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
            
        if len(tempProduct2) != 0 :
            
            kalıp2 = {}

            if(tempProduct2[0]['site2']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani2']= puani
                toplu['fiyat2']= float(fiyat)
                toplu['prodLink2']= prodLink
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
            
            elif(tempProduct2[0]['site3']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani3']= puani
                toplu['fiyat3']= float(fiyat)
                toplu['prodLink3']= prodLink
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
            elif(tempProduct2[0]['site4']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani4']= puani
                toplu['fiyat4']= float(fiyat)
                toplu['prodLink4']= prodLink
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
            elif(tempProduct2[0]['site5']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani5']= puani
                toplu['fiyat5']= float(fiyat)
                toplu['prodLink5']= prodLink
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
            elif(tempProduct2[0]['site6']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani6']= puani
                toplu['fiyat6']= float(fiyat)
                toplu['prodLink6']= prodLink
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
           

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
        myClient2 = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']
        mydb2 = myClient2['WebScraping']

        myCollection = mydb['ecommerce_matchproducts']
        myCollection2 = mydb['shopping_matchproducts']

        myCollection.delete_one({'modelNo':modelNo})
        base = {}
        base['modelNo']= modelNo
        tempProduct2 = myCollection2.find(base)
        tempProduct2 = list(tempProduct2)

        if len(tempProduct2) != 0 :
            
            kalıp2 = {}

            if(tempProduct2[0]['site2']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani2']= ""
                toplu['fiyat2']= ""
                toplu['prodLink2']= ""
                toplu['site2']= ""
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
            
            elif(tempProduct2[0]['site3']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani3']= ""
                toplu['fiyat3']= ""
                toplu['prodLink3']= ""
                toplu['site3'] = ""
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
                
            elif(tempProduct2[0]['site4']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani4']= ""
                toplu['fiyat4']= ""
                toplu['prodLink4']= ""
                toplu['site4'] = ""
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
                
            elif(tempProduct2[0]['site5']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani5']= ""
                toplu['fiyat5']= ""
                toplu['prodLink5']= ""
                toplu['site5']= ""
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
                
            elif(tempProduct2[0]['site6']=='41LaptopStore'):
                
                kalıp2 = {}

                kalıp2['modelNo']=modelNo
                toplu = {}
                toplu['puani6']= ""
                toplu['fiyat6']= ""
                toplu['prodLink6']= ""
                toplu['site6'] = ""
                kalıp = {}

                kalıp['$set'] = toplu
                myCollection2.update_one(kalıp2, kalıp)
           

        print('Isleminiz Gerceklesmistir')

        return redirect('home')

    return render(request, "crud/delete.html")