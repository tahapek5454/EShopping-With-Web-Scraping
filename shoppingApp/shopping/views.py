from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Products, MatchProducts
import pymongo 
from pymongo import MongoClient
import threading
import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# tablodaki verileri cekip canlıya atmak icin

# Create your views here.
# burada beliritilen linklerde neler gozukecegini soyleriz
class Database:
    
    client=MongoClient('mongodb://{0}:{0}@localhost:27017'.format('abvag','abvag'))
    db=client["WebScraping"]
    mycol=db["shopping_matchproducts"]
    
    def __init__(self) -> None:     
        pass
    
    def add_dict_product(self,prod_dict):
        self.mycol.insert_many(prod_dict)
        
    def add_one_product(self,dict):
        self.mycol.insert_one(dict)
        
    def control_add_product(self,prod_dict):
        
        prod= self.mycol.find()
        if(prod==None):
            
            self.add_dict_product(prod_dict)
            
        else:
            for p in prod_dict:
                    
                    for a in prod:
                        
                        if(a['prodLink']==p['prodLink']):
                            
                            self.delete_product(a)
                            break
               
                    self.add_one_product(p)
                  
    def delete_product(self,dict):
        
        self.mycol.delete_one(dict)
            
    def delete_col(self):
        
        self.mycol.delete_many({})

class Database2:
    
    client=MongoClient('mongodb://{0}:{0}@localhost:27017'.format('abvag','abvag'))
    db=client["WebScraping"]
    mycol=db["ecommerce_matchproducts"]
    
    def __init__(self) -> None:     
        pass
    
    def add_dict_product(self,prod_dict):
        self.mycol.insert_many(prod_dict)
        
    def add_one_product(self,dict):
        self.mycol.insert_one(dict)
        
    def control_add_product(self,prod_dict):
        
        prod= self.mycol.find()
        if(prod==None):
            
            self.add_dict_product(prod_dict)
            
        else:
            for p in prod_dict:
                    
                    for a in prod:
                        
                        if(a['prodLink']==p['prodLink']):
                            
                            self.delete_product(a)
                            break
               
                    self.add_one_product(p)
                  
    def delete_product(self,dict):
        
        self.mycol.delete_one(dict)
            
    def delete_col(self):
        
        self.mycol.delete_many({})  



class GetDatasWithThread:

    teknosaAll=[]
    trendYolAll=[]
    n11All=[]
    cicekSepetiAll=[]
    hepsiBuradaAll=[]

    def __init__(self) -> None:
        pass

    def getTeknosaAll(self):
        #print('Teknosa cekerim')
        self.teknosaAll = Products.objects.filter(site="Teknosa")

    def getTrendYolAll(self):
        #print('Trendyol cekerim')
        self.trendYolAll = Products.objects.filter(site="Trendyol")

    def getN11All(self):
        #print('N11 cekerim')
        self.n11All = Products.objects.filter(site="n11")
   
    def getCicekSepetiAll(self):
        #print('Cicek cekerim')
        self.cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
        
    def getHepsiBuradaAll(self):
        #print('Hepsi cekerim')
        self.hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")
    
    def AgetTeknosaAll(self):
        print('Teknosa cekerim')
        self.teknosaAll = Products.objects.filter(site="Teknosa").order_by('fiyat')

    def AgetTrendYolAll(self):
        print('Trendyol cekerim')
        self.trendYolAll = Products.objects.filter(site="Trendyol").order_by('fiyat')

    def AgetN11All(self):
        print('N11 cekerim')
        self.n11All = Products.objects.filter(site="n11").order_by('fiyat')
        
    def AgetCicekSepetiAll(self):
        print('Cicek cekerim')
        self.cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti").order_by('fiyat')
            
    def AgetHepsiBuradaAll(self):
        print('Hepsi cekerim')
        self.hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")
    
    def AgetTeknosaAll(self):
        print('Teknosa cekerim')
        self.teknosaAll = Products.objects.filter(site="Teknosa").order_by('fiyat')

    def AgetTrendYolAll(self):
        print('Trendyol cekerim')
        self.trendYolAll = Products.objects.filter(site="Trendyol").order_by('fiyat')

    def AgetN11All(self):
        print('N11 cekerim')
        self.n11All = Products.objects.filter(site="n11").order_by('fiyat')
        
    def AgetCicekSepetiAll(self):
        print('Cicek cekerim')
        self.cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti").order_by('fiyat')
            
    def AgetHepsiBuradaAll(self):
        print('Hepsi cekerim')
        self.hepsiBuradaAll = Products.objects.filter(site="Hepsiburada").order_by('fiyat')
    
    def DgetTeknosaAll(self):
        print('Teknosa cekerim')
        self.teknosaAll = Products.objects.filter(site="Teknosa").order_by('-fiyat')

    def DgetTrendYolAll(self):
        print('Trendyol cekerim')
        self.trendYolAll = Products.objects.filter(site="Trendyol").order_by('-fiyat')

    def DgetN11All(self):
        print('N11 cekerim')
        self.n11All = Products.objects.filter(site="n11").order_by('-fiyat')
        
    def DgetCicekSepetiAll(self):
        print('Cicek cekerim')
        self.cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti").order_by('-fiyat')
       
    def DgetHepsiBuradaAll(self):
        print('Hepsi cekerim')
        self.hepsiBuradaAll = Products.objects.filter(site="Hepsiburada").order_by('-fiyat')
    
    def SDgetTeknosaAll(self):
        print('Teknosa cekerim')
        self.teknosaAll = Products.objects.filter(site="Teknosa").order_by('-puani')

    def SDgetTrendYolAll(self):
        print('Trendyol cekerim')
        self.trendYolAll = Products.objects.filter(site="Trendyol").order_by('-puani')

    def SDgetN11All(self):
        print('N11 cekerim')
        self.n11All = Products.objects.filter(site="n11").order_by('-puani')
        
    def SDgetCicekSepetiAll(self):
        print('Cicek cekerim')
        self.cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti").order_by('-puani')
       
    def SDgetHepsiBuradaAll(self):
        print('Hepsi cekerim')
        self.hepsiBuradaAll = Products.objects.filter(site="Hepsiburada").order_by('-puani')

def home(request):
    gdwt = GetDatasWithThread()
            
    
    # client=MongoClient("mongodb://{0}:{0}@localhost:27017".format('abvag','abvag'))
    # db=client['WebScraping']
    # col=db['shopping_products']

    # prods=col.find({'puani':0})

    # for x in prods:
    #     col.update_one({'prodLink':x['prodLink']},{'$set':{'puani':round(random.uniform(3,5),2)}})

    
    
    
    # teknosaAllThread = threading.Thread(target=gdwt.getTeknosaAll)
    # trendYolAllThread = threading.Thread(target=gdwt.getTrendYolAll)
    # n11AllThread = threading.Thread(target=gdwt.getN11All)
    # cicekSepetiAllThread = threading.Thread(target=gdwt.getCicekSepetiAll)
    # hepsiBuradaAllThread = threading.Thread(target=gdwt.getHepsiBuradaAll)

    # teknosaAll = Products.objects.filter(site="Teknosa")
    # trendYolAll = Products.objects.filter(site="Trendyol")
    # n11All = Products.objects.filter(site="n11")
    # cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
    # hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")

    
    # teknosaAllThread.start()

    # trendYolAllThread.start()
    # n11AllThread.start()
    # cicekSepetiAllThread.start()
    # hepsiBuradaAllThread.start()

    
    # teknosaAllThread.join()

    # trendYolAllThread.join()
    # n11AllThread.join()
    # cicekSepetiAllThread.join()
    # hepsiBuradaAllThread.join()


    # print("Teknosa  "+ str(len(gdwt.teknosaAll)))
    # print("Trend Yol    " + str(len(gdwt.trendYolAll)))
    # print("N11  " + str(len(gdwt.n11All)))
    # print("Cicek Sepeti     "+ str(len(gdwt.cicekSepetiAll)))
    # print("Hepsi Burda  " + str(len(gdwt.hepsiBuradaAll)))
    
    

    allProducts = MatchProducts.objects.all()

    # kategorilerin ekranda sıralanmasıyla alakalı
    # model adini ekledim
    marka = set()
    modelAdi = set()
    isletimSistemi = set()
    islemciTipi = set()
    islemciNesli = set()
    ram = set()
    diskTuru = set()
    ekranBoyu = set()
    diskBoyutu = set()


    
    # kategori filter

    for item in allProducts:
 
        if item.marka != "":
            # print('')
            # print(item.marka)
            # print(item.marka.capitalize())
            # print('')
            if item.marka == "ASUS":
                marka.add(item.marka.capitalize())
            elif item.marka == "Hp":
                marka.add(item.marka.upper())
            else:
                marka.add(item.marka)
        
        if item.modelAdi !="":
            print(item.modelAdi)
            modelAdi.add(item.modelAdi)


        if item.isletimSistemi !="":
            # print('')
            # print(item.isletimSistemi)
            # print(item.isletimSistemi.capitalize())
            # print('')
            isletimSistemi.add(item.isletimSistemi)
        
        if item.islemciTipi != "":
            # print('')
            # print(item.islemciTipi)
            # print(item.islemciTipi.title())
            # print('')
            islemciTipi.add(item.islemciTipi)

        if item.islemciNesli != "":
            if(item.islemciNesli !='Yok'):
                islemciNesli.add(int(item.islemciNesli))
            else:
                islemciNesli.add(0)
            
        
        if item.ram != "":
            # print('')
            # print(item.ram)
            # print(item.ram.title())
            # print('')
            ram.add(item.ram)
        
        if item.diskTuru != "":
            # print('')
            # print(item.diskTuru)
            # print(item.diskTuru.title())
            # print('')
            diskTuru.add(item.diskTuru)
        
        if item.ekranBoyu != "":
            # print('')
            # print(item.ekranBoyu)
            # print(item.ekranBoyu.capitalize())
            # print('')
            ekranBoyu.add(item.ekranBoyu)
        
        if item.diskBoyutu != "":
            # print('')
            # print(item.diskBoyutu)
            # print(item.diskBoyutu.capitalize())
            # print('')
            diskBoyutu.add(item.diskBoyutu)
        
    

    # with open('Kategoriler.txt','w', encoding="utf-8") as f:

    #     for item in marka:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciNesli:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciTipi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ekranBoyu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskBoyutu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ram:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in isletimSistemi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskTuru:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in modelAdi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')
       
    
     
   
        
        


    marka=sorted(marka)
    islemciNesli=sorted(islemciNesli)
    islemciTipi=sorted(islemciTipi)
    ekranBoyu=sorted(ekranBoyu)
    diskBoyutu=sorted(diskBoyutu)
    ram=sorted(ram)
    
    
    # print(type(Products.objects.filter(site="Teknosa")))
    # print("Set Marka uzunlugu "+str(len(marka)))
    # print("Sets Marka")
    # print(marka)

            


    # for eslesen in allProducts:

    #     print("Toplam eslesen "+ str(len(eslesen)))
    #     for i in eslesen:
    #         print(i.site)
    #     print("*"*100)
    

    print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

    # for a in allProducts:
    #     for b in a:
    #         print(b.site)
    #     break
    posts=allProducts
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    dynamicVar = {
        'products': PostsFinal,
        'markas':marka,
        'isletimSistemis' : isletimSistemi,
        'islemciTipis' : islemciTipi,
        'islemciNeslis' : islemciNesli,
        'rams': ram,
        'diskTurus': diskTuru,
        'ekranBoyus': ekranBoyu,
        'diskBoyutus': diskBoyutu,
        'modelAdis': modelAdi    
    }
    #tum urunleri al dedik
    

    #render bize gelen requeste gore templatelerden dosya arıyor
    #spesifik bir yerden aramasını istedigimizden template altında dosya olusturduk
    # return render(request, "shopping/index.html", dynamicVar) 
    return render(request, "shopping/index.html", dynamicVar)

def productDetails(request, id):

    # mesela biz id yi de request gondermek istiyoruz
    # onu bir dict yapısında 3. parametre olarak gonderebilirz
    # ilgili yerde kullanımı {{ }} icersinde olur

    # simdilik id ye gore cekicem ama isin icine birden fazla gelince model no olucak
    # products = DenemeProduct.objects.filter(id = id)

    # su an tek bir veri gelse de bu veri [veri] seklinde bir dizi elemanı olarak geliyor

    product = MatchProducts.objects.get(id=id)

    print('*****************************')
    print(product.modelAdi)
    print(product.islemciTipi)
    print(product.islemciNesli)
    print(product.marka)
    print(product.site)
    print('*****************************')

    

    dynamicVar = {
        'product' : product
    }

    
    

    # dynamicVar = {
    #     'products': ""
    # }
    # return render(request, "shopping/productDetails.html", dynamicVar)
    return render(request, "shopping/productDetails.html", dynamicVar)

def filterByCategory(request):
    gdwt = GetDatasWithThread()
    flag = False
    base = {}
    
    if request.method == "POST":
       
        print("Posta girdim haberin olsun")
        
        selectedMarka = request.POST.getlist('marka')
        selectedIsletimSistemi = request.POST.getlist('isletimSistemi')
        selectedIslemciTipi = request.POST.getlist('islemciTipi')
        selectedIslemciNesli = request.POST.getlist('islemciNesli')
        selectedRam = request.POST.getlist('ram')
        selectedDiskTuru = request.POST.getlist('diskTuru')
        selectedEkranBoyu = request.POST.getlist('ekranBoyu')
        selectedDiskBoyutu = request.POST.getlist('diskBoyutu')
        selectedModelAdi = request.POST.getlist('modelAdi')

        
        """
        c ={}
        c['marka']={ "$in" : ["Monster", "Asus"]}
        c['modelAdi'] = {"$in" : ["Abra"]}
        """
        if len(selectedMarka) != 0:
            flag = True
            base['marka'] = {"$in" : selectedMarka}               
        if len(selectedIsletimSistemi) != 0:
            flag = True
            base['isletimSistemi'] = {"$in" : selectedIsletimSistemi}
        if len(selectedIslemciTipi) != 0:
            flag = True
            base['islemciTipi'] = {"$in" : selectedIslemciTipi}
        if len(selectedIslemciNesli) != 0:
            flag = True
            base['islemciNesli'] = {"$in" : selectedIslemciNesli}
        if len(selectedRam) != 0:
            flag = True
            base['ram'] = {"$in" : selectedRam}
        if len(selectedDiskTuru) != 0:
            flag = True
            base['diskTuru'] = {"$in" : selectedDiskTuru}
        if len(selectedEkranBoyu) != 0:
            flag = True
            base['ekranBoyu'] = {"$in" : selectedEkranBoyu}
        if len(selectedDiskBoyutu) != 0:
            flag = True
            base['diskBoyutu'] = {"$in" : selectedDiskBoyutu}
        if len(selectedModelAdi) != 0:
            flag = True
            base['modelAdi'] = {"$in" : selectedModelAdi}
        
        base['site']={"$in" : ["Teknosa"]}

    print(base)

    if flag:
        
        
        # baglanma islemi
        myClient = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']


        myCollection = mydb['shopping_matchproducts']

        allProducts = myCollection.find(base)

        allProducts = list(allProducts)


       
        print(len(allProducts))

        if len(allProducts) == 0:
            # filterdan veri gelmediyse
            print('Home gitmeliyim')
            return redirect('home')

        else:

            # start scrapping
            # trendYolAllThread = threading.Thread(target=gdwt.getTrendYolAll)
            # n11AllThread = threading.Thread(target=gdwt.getN11All)
            # cicekSepetiAllThread = threading.Thread(target=gdwt.getCicekSepetiAll)
            # hepsiBuradaAllThread = threading.Thread(target=gdwt.getHepsiBuradaAll)
            
            # trendYolAllThread.start()
            # n11AllThread.start()
            # cicekSepetiAllThread.start()
            # hepsiBuradaAllThread.start()

                        
            # trendYolAllThread.join()
            # n11AllThread.join()
            # cicekSepetiAllThread.join()
            # hepsiBuradaAllThread.join()


            


            # match data
            # for i in teknosa:
            #     # print(i)
            #     equalsProduct = []
            #     equalsProduct.append(i)

            #     for j in gdwt.trendYolAll:
            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     for j in gdwt.n11All:

            #         # if j.modelNo!="Yok" and j.modelNo!="Belirtilmemiş" and j.modelNo!="" :
            #         #     if j.modelNo == i.modelNo:
            #         #         equalsProduct.append(j)
            #         #         break

            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     for j in gdwt.cicekSepetiAll:
            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     for j in gdwt.hepsiBuradaAll:
            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     if len(equalsProduct) >=2:
            #         allProducts.append(equalsProduct)


            print('Filterdan sonra gelip de eslesen verilerin toplamı '+str(len(allProducts)))



            # kategorilerin ekranda sıralanmasıyla alakalı
            marka = set()
            isletimSistemi = set()
            islemciTipi = set()
            islemciNesli = set()
            ram = set()
            diskTuru = set()
            ekranBoyu = set()
            diskBoyutu = set()
            modelAdi = set()

            for item in allProducts:
          
                if item['marka'] != "":
                    # print('')
                    # print(item['marka'])
                    # print(item['marka'].capitalize())
                    # print('')
                    if item["marka"] == "ASUS":
                        marka.add(item["marka"].capitalize())
                    elif item["marka"] == "Hp":
                        marka.add(item["marka"].upper())
                    else:
                        marka.add(item["marka"])

                if item['isletimSistemi'] !="":
                    # print('')
                    # print(item['isletimSistemi'])
                    # print(item['isletimSistemi'].capitalize())
                    # print('')
                    isletimSistemi.add(item['isletimSistemi'])
                
                if item['islemciTipi'] != "":
                    # print('')
                    # print(item['islemciTipi'])
                    # print(item['islemciTipi'].title())
                    # print('')
                    
                    islemciTipi.add(item['islemciTipi'])

                if item['islemciNesli'] != "":
                    if(item['islemciNesli'] !='Yok'):
                        islemciNesli.add(int(item['islemciNesli']))
                    else:
                        islemciNesli.add(0)
                
                if item['ram'] != "":
                    ram.add(item['ram'])
                
                if item['diskTuru'] != "":
                    # print('')
                    # print(item['diskTuru'])
                    # print(item['diskTuru'].title())
                    # print('')
                    diskTuru.add(item['diskTuru'])
                
                if item['ekranBoyu'] != "":
                    # print('')
                    # print(item['ekranBoyu'])
                    # print(item['ekranBoyu'].capitalize())
                    # print('')
                    ekranBoyu.add(item['ekranBoyu'])
                
                if item['diskBoyutu'] != "":
                    # print('')
                    # print(item['diskBoyutu'])
                    # print(item['diskBoyutu'].capitalize())
                    # print('')
                    diskBoyutu.add(item['diskBoyutu'])

                if item['modelAdi'] != "":
                    
                    modelAdi.add(item['modelAdi'])
                
            
            marka=sorted(marka)
            islemciNesli=sorted(islemciNesli)
            islemciTipi=sorted(islemciTipi)
            ekranBoyu=sorted(ekranBoyu)
            diskBoyutu=sorted(diskBoyutu)
            ram=sorted(ram)
            
            
            # print(type(Products.objects.filter(site="Teknosa")))
            # print("Set Marka uzunlugu "+str(len(marka)))
            # print("Sets Marka")
            # print(marka)

                    


            # for eslesen in allProducts:

            #     print("Toplam eslesen "+ str(len(eslesen)))
            #     for i in eslesen:
            #         print(i.site)
            #     print("*"*100)
            

            print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

            # for a in allProducts:
            #     for b in a:
            #         print(b.site)
            #     break
            posts=allProducts
            page = request.GET.get('page')
            num_of_item= 20
            paginator= Paginator(posts,num_of_item)
            PostsFinal=paginator.get_page(page)
            
            dynamicVar = {
                'products': PostsFinal,
                'markas':marka,
                'isletimSistemis' : isletimSistemi,
                'islemciTipis' : islemciTipi,
                'islemciNeslis' : islemciNesli,
                'rams': ram,
                'diskTurus': diskTuru,
                'ekranBoyus': ekranBoyu,
                'diskBoyutus': diskBoyutu,
                'modelAdis' : modelAdi  
            }
            #tum urunleri al dedik
            

            #render bize gelen requeste gore templatelerden dosya arıyor
            #spesifik bir yerden aramasını istedigimizden template altında dosya olusturduk
            # return render(request, "shopping/index.html", dynamicVar) 
            return render(request, "shopping/index.html", dynamicVar)

            

    else:
        return redirect('home')

def filterWithSearchBar(request):
    gdwt = GetDatasWithThread()
    flag = False
    base = {}
    
    if request.method == "POST":
       
        print("Search Bar Postuna girdim haberin olsun")
        
        barValue = request.POST["searchBar"]
        barValue = str(barValue)
        print("Bardan gelen value = "+barValue)

        
        """
        c ={}
        c['marka']={ "$in" : ["Monster", "Asus"]}
        c['modelAdi'] = {"$in" : ["Abra"]}
        """
        if len(barValue) > 0:
            flag = True
        base['site']={"$in" : ["Teknosa"]}

    print(base)

    if flag:
        
        
        # baglanma islemi
        myClient = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']


        myCollection = mydb['shopping_matchproducts']

        tempProduct = myCollection.find(base)
        tempProduct = list(tempProduct)
        

        
        allProducts=[]

        for item in tempProduct:

            if barValue == "Teknosa":
                allProducts.append(item)
            
            elif barValue == "Trendyol":
                if item['site2'] == "Trendyol":
                    allProducts.append(item)
                elif item['site3'] == "Trendyol":
                    allProducts.append(item)
                elif item['site4'] == "Trendyol":
                    allProducts.append(item)
                elif item['site5'] == "Trendyol":
                    allProducts.append(item)
                elif item['site6'] == "Trendyol":
                    allProducts.append(item)
            
            elif barValue == "Hepsiburada":
                if item['site2'] == "Hepsiburada":
                    allProducts.append(item)
                elif item['site3'] == "Hepsiburada":
                    allProducts.append(item)
                elif item['site4'] == "Hepsiburada":
                    allProducts.append(item)
                elif item['site5'] == "Hepsiburada":
                    allProducts.append(item)
                elif item['site6'] == "Hepsiburada":
                    allProducts.append(item)
            
            elif barValue == "n11":
                if item['site2'] == "n11":
                    allProducts.append(item)
                elif item['site3'] == "n11":
                    allProducts.append(item)
                elif item['site4'] == "n11":
                    allProducts.append(item)
                elif item['site5'] == "n11":
                    allProducts.append(item)
                elif item['site6'] == "n11":
                    allProducts.append(item)
            
            elif barValue == "ÇiçekSepeti":
                if item['site2'] == "ÇiçekSepeti":
                    allProducts.append(item)
                elif item['site3'] == "ÇiçekSepeti":
                    allProducts.append(item)
                elif item['site4'] == "ÇiçekSepeti":
                    allProducts.append(item)
                elif item['site5'] == "ÇiçekSepeti":
                    allProducts.append(item)
                elif item['site6'] == "ÇiçekSepeti":
                    allProducts.append(item)



            elif item['prodTitle'].find(barValue) !=-1:
                print('Title icinde buldum')
                allProducts.append(item)

        print("allProdycts uzunlugu "+ str(len(allProducts)))
        print(allProducts)
        if len(allProducts) == 0:
            # filterdan veri gelmediyse
            print('Home gitmeliyim')
            return redirect('home')

        else:

            # start scrapping
            # trendYolAllThread = threading.Thread(target=gdwt.getTrendYolAll)
            # n11AllThread = threading.Thread(target=gdwt.getN11All)
            # cicekSepetiAllThread = threading.Thread(target=gdwt.getCicekSepetiAll)
            # hepsiBuradaAllThread = threading.Thread(target=gdwt.getHepsiBuradaAll)
            
            # trendYolAllThread.start()
            # n11AllThread.start()
            # cicekSepetiAllThread.start()
            # hepsiBuradaAllThread.start()

                        
            # trendYolAllThread.join()
            # n11AllThread.join()
            # cicekSepetiAllThread.join()
            # hepsiBuradaAllThread.join()


           


            # match data
            # for i in teknosa:
            #     # print(i)
            #     equalsProduct = []
            #     equalsProduct.append(i)

            #     for j in gdwt.trendYolAll:
            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     for j in gdwt.n11All:

            #         # if j.modelNo!="Yok" and j.modelNo!="Belirtilmemiş" and j.modelNo!="" :
            #         #     if j.modelNo == i.modelNo:
            #         #         equalsProduct.append(j)
            #         #         break

            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     for j in gdwt.cicekSepetiAll:
            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     for j in gdwt.hepsiBuradaAll:
            #         if j.prodTitle.lower().find(i['modelNo'].lower()) !=-1:
            #             equalsProduct.append(j)
            #             break
                
            #     if len(equalsProduct) >=2:
            #         allProducts.append(equalsProduct)


            print('Filterdan sonra gelip de eslesen verilerin toplamı '+str(len(allProducts)))



            # kategorilerin ekranda sıralanmasıyla alakalı
            marka = set()
            isletimSistemi = set()
            islemciTipi = set()
            islemciNesli = set()
            ram = set()
            diskTuru = set()
            ekranBoyu = set()
            diskBoyutu = set()
            modelAdi = set()

            for eslesen in allProducts:

                if item['marka'] != "":
                    # print('')
                    # print(item['marka'])
                    # print(item['marka'].capitalize())
                    # print('')
                    if item["marka"] == "ASUS":
                        marka.add(item["marka"].capitalize())
                    elif item["marka"] == "Hp":
                        marka.add(item["marka"].upper())
                    else:
                        marka.add(item["marka"])

                if item['isletimSistemi'] !="":
                    # print('')
                    # print(item['isletimSistemi'])
                    # print(item['isletimSistemi'].capitalize())
                    # print('')
                    isletimSistemi.add(item['isletimSistemi'])
                
                if item['islemciTipi'] != "":
                    # print('')
                    # print(item['islemciTipi'])
                    # print(item['islemciTipi'].title())
                    # print('')
                    
                    islemciTipi.add(item['islemciTipi'])

                if item['islemciNesli'] != "":
                    if(item['islemciNesli'] !='Yok'):
                        islemciNesli.add(int(item['islemciNesli']))
                    else:
                        islemciNesli.add(0)
                
                if item['ram'] != "":
                    ram.add(item['ram'])
                
                if item['diskTuru'] != "":
                    # print('')
                    # print(item['diskTuru'])
                    # print(item['diskTuru'].title())
                    # print('')
                    diskTuru.add(item['diskTuru'])
                
                if item['ekranBoyu'] != "":
                    # print('')
                    # print(item['ekranBoyu'])
                    # print(item['ekranBoyu'].capitalize())
                    # print('')
                    ekranBoyu.add(item['ekranBoyu'])
                
                if item['diskBoyutu'] != "":
                    # print('')
                    # print(item['diskBoyutu'])
                    # print(item['diskBoyutu'].capitalize())
                    # print('')
                    diskBoyutu.add(item['diskBoyutu'])

                if item['modelAdi'] != "":
                    
                    modelAdi.add(item['modelAdi'])
                
            
            marka=sorted(marka)
            islemciNesli=sorted(islemciNesli)
            islemciTipi=sorted(islemciTipi)
            ekranBoyu=sorted(ekranBoyu)
            diskBoyutu=sorted(diskBoyutu)
            ram=sorted(ram)
            
            
            # print(type(Products.objects.filter(site="Teknosa")))
            # print("Set Marka uzunlugu "+str(len(marka)))
            # print("Sets Marka")
            # print(marka)

                    


            # for eslesen in allProducts:

            #     print("Toplam eslesen "+ str(len(eslesen)))
            #     for i in eslesen:
            #         print(i.site)
            #     print("*"*100)
            

            print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

            # for a in allProducts:
            #     for b in a:
            #         print(b.site)
            #     break
            posts=allProducts
            page = request.GET.get('page')
            num_of_item= 20
            paginator= Paginator(posts,num_of_item)
            PostsFinal=paginator.get_page(page)
            
            dynamicVar = {
                'products': PostsFinal,
                'markas':marka,
                'isletimSistemis' : isletimSistemi,
                'islemciTipis' : islemciTipi,
                'islemciNeslis' : islemciNesli,
                'rams': ram,
                'diskTurus': diskTuru,
                'ekranBoyus': ekranBoyu,
                'diskBoyutus': diskBoyutu,
                'modelAdis' : modelAdi  
            }
            #tum urunleri al dedik
            

            #render bize gelen requeste gore templatelerden dosya arıyor
            #spesifik bir yerden aramasını istedigimizden template altında dosya olusturduk
            # return render(request, "shopping/index.html", dynamicVar) 
            return render(request, "shopping/index.html", dynamicVar)

            

    else:
        return redirect('home')

def DescSortProd(request):
    
    gdwt = GetDatasWithThread()

    # teknosaAllThread = threading.Thread(target=gdwt.DgetTeknosaAll)
    # trendYolAllThread = threading.Thread(target=gdwt.DgetTrendYolAll)
    # n11AllThread = threading.Thread(target=gdwt.DgetN11All)
    # cicekSepetiAllThread = threading.Thread(target=gdwt.DgetCicekSepetiAll)
    # hepsiBuradaAllThread = threading.Thread(target=gdwt.DgetHepsiBuradaAll)

    # teknosaAll = Products.objects.filter(site="Teknosa")
    # trendYolAll = Products.objects.filter(site="Trendyol")
    # n11All = Products.objects.filter(site="n11")
    # cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
    # hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")

    # teknosaAllThread.start()
    # trendYolAllThread.start()
    # n11AllThread.start()
    # cicekSepetiAllThread.start()
    # hepsiBuradaAllThread.start()

    # teknosaAllThread.join()
    # trendYolAllThread.join()
    # n11AllThread.join()
    # cicekSepetiAllThread.join()
    # hepsiBuradaAllThread.join()


    # print("Teknosa  "+ str(len(gdwt.teknosaAll)))
    # print("Trend Yol    " + str(len(gdwt.trendYolAll)))
    # print("N11  " + str(len(gdwt.n11All)))
    # print("Cicek Sepeti     "+ str(len(gdwt.cicekSepetiAll)))
    # print("Hepsi Burda  " + str(len(gdwt.hepsiBuradaAll)))
    
    
    # allProducts = []

    # for i in gdwt.teknosaAll:

    #     equalsProduct = []
    #     equalsProduct.append(i)

    #     for j in gdwt.trendYolAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.n11All:

    #         # if j.modelNo!="Yok" and j.modelNo!="Belirtilmemiş" and j.modelNo!="" :
    #         #     if j.modelNo == i.modelNo:
    #         #         equalsProduct.append(j)
    #         #         break

    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.cicekSepetiAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.hepsiBuradaAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     if len(equalsProduct) >=2:
    #         allProducts.append(equalsProduct)
        
    
    # marka = set()
    # isletimSistemi = set()
    # islemciTipi = set()
    # islemciNesli = set()
    # ram = set()
    # diskTuru = set()
    # ekranBoyu = set()
    # diskBoyutu = set()

    # for eslesen in allProducts:

    #     for item in eslesen:

    #         if item.site == 'Teknosa':
    #             if item.marka != "":
                    
    #                 marka.add(item.marka.capitalize())

    #             if item.isletimSistemi !="":
    #                 isletimSistemi.add(item.isletimSistemi.capitalize())
                
    #             if item.islemciTipi != "":
    #                 islemciTipi.add(item.islemciTipi.title())

    #             if item.islemciNesli != "":
    #                 if(item.islemciNesli !='Yok'):
    #                     islemciNesli.add(int(item.islemciNesli))
    #                 else:
    #                     islemciNesli.add(0)
                
    #             if item.ram != "":
    #                 ram.add(int(item.ram.split(' ')[0]))
                
    #             if item.diskTuru != "":
    #                 diskTuru.add(item.diskTuru.title())
                
    #             if item.ekranBoyu != "":
    #                 ekranBoyu.add(item.ekranBoyu.capitalize())
                
    #             if item.diskBoyutu != "":
    #                 diskBoyutu.add(item.diskBoyutu.capitalize())
    #             break
    
    # marka=sorted(marka)
    # islemciNesli=sorted(islemciNesli)
    # islemciTipi=sorted(islemciTipi)
    # ekranBoyu=sorted(ekranBoyu)
    # diskBoyutu=sorted(diskBoyutu)
    # ram=sorted(ram)
    
    
    # print(type(Products.objects.filter(site="Teknosa")))
    # print("Set Marka uzunlugu "+str(len(marka)))
    # print("Sets Marka")
    # print(marka)

            


    # for eslesen in allProducts:

    #     print("Toplam eslesen "+ str(len(eslesen)))
    #     for i in eslesen:
    #         print(i.site)
    #     print("*"*100)
    

    # print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

    # for a in allProducts:
    #     for b in a:
    #         print(b.site)
    #     break
    allProducts = MatchProducts.objects.all().order_by("-fiyat")

    
    for i in allProducts:
        print('***********************************')
        print(i)
        print('***********************************')

    # kategorilerin ekranda sıralanmasıyla alakalı
    # model adini ekledim
    marka = set()
    modelAdi = set()
    isletimSistemi = set()
    islemciTipi = set()
    islemciNesli = set()
    ram = set()
    diskTuru = set()
    ekranBoyu = set()
    diskBoyutu = set()


    
    # kategori filter

    for item in allProducts:
 
        if item.marka != "":
            # print('')
            # print(item.marka)
            # print(item.marka.capitalize())
            # print('')
            if item.marka == "ASUS":
                marka.add(item.marka.capitalize())
            elif item.marka == "Hp":
                marka.add(item.marka.upper())
            else:
                marka.add(item.marka)
        
        if item.modelAdi !="":
            print(item.modelAdi)
            modelAdi.add(item.modelAdi)


        if item.isletimSistemi !="":
            # print('')
            # print(item.isletimSistemi)
            # print(item.isletimSistemi.capitalize())
            # print('')
            isletimSistemi.add(item.isletimSistemi)
        
        if item.islemciTipi != "":
            # print('')
            # print(item.islemciTipi)
            # print(item.islemciTipi.title())
            # print('')
            islemciTipi.add(item.islemciTipi)

        if item.islemciNesli != "":
            if(item.islemciNesli !='Yok'):
                islemciNesli.add(int(item.islemciNesli))
            else:
                islemciNesli.add(0)
            
        
        if item.ram != "":
            # print('')
            # print(item.ram)
            # print(item.ram.title())
            # print('')
            ram.add(item.ram)
        
        if item.diskTuru != "":
            # print('')
            # print(item.diskTuru)
            # print(item.diskTuru.title())
            # print('')
            diskTuru.add(item.diskTuru)
        
        if item.ekranBoyu != "":
            # print('')
            # print(item.ekranBoyu)
            # print(item.ekranBoyu.capitalize())
            # print('')
            ekranBoyu.add(item.ekranBoyu)
        
        if item.diskBoyutu != "":
            # print('')
            # print(item.diskBoyutu)
            # print(item.diskBoyutu.capitalize())
            # print('')
            diskBoyutu.add(item.diskBoyutu)
        
    

    # with open('Kategoriler.txt','w', encoding="utf-8") as f:

    #     for item in marka:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciNesli:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciTipi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ekranBoyu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskBoyutu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ram:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in isletimSistemi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskTuru:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in modelAdi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')
       
    
     
   
        
        


    marka=sorted(marka)
    islemciNesli=sorted(islemciNesli)
    islemciTipi=sorted(islemciTipi)
    ekranBoyu=sorted(ekranBoyu)
    diskBoyutu=sorted(diskBoyutu)
    ram=sorted(ram)
    
    
    # print(type(Products.objects.filter(site="Teknosa")))
    # print("Set Marka uzunlugu "+str(len(marka)))
    # print("Sets Marka")
    # print(marka)

            


    # for eslesen in allProducts:

    #     print("Toplam eslesen "+ str(len(eslesen)))
    #     for i in eslesen:
    #         print(i.site)
    #     print("*"*100)
    

    print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

    # for a in allProducts:
    #     for b in a:
    #         print(b.site)
    #     break
    posts=allProducts
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    dynamicVar = {
        'products': PostsFinal,
        'markas':marka,
        'isletimSistemis' : isletimSistemi,
        'islemciTipis' : islemciTipi,
        'islemciNeslis' : islemciNesli,
        'rams': ram,
        'diskTurus': diskTuru,
        'ekranBoyus': ekranBoyu,
        'diskBoyutus': diskBoyutu,
        'modelAdis': modelAdi    
    }
    #tum urunleri al dedik
    #tum urunleri al dedik

    #render bize gelen requeste gore templatelerden dosya arıyor
    #spesifik bir yerden aramasını istedigimizden template altında dosya olusturduk
    # return render(request, "shopping/index.html", dynamicVar) 
    return render(request, "shopping/index.html", dynamicVar)

def DescStarProd(request):
        
    gdwt = GetDatasWithThread()

    # teknosaAllThread = threading.Thread(target=gdwt.DgetTeknosaAll)
    # trendYolAllThread = threading.Thread(target=gdwt.DgetTrendYolAll)
    # n11AllThread = threading.Thread(target=gdwt.DgetN11All)
    # cicekSepetiAllThread = threading.Thread(target=gdwt.DgetCicekSepetiAll)
    # hepsiBuradaAllThread = threading.Thread(target=gdwt.DgetHepsiBuradaAll)

    # teknosaAll = Products.objects.filter(site="Teknosa")
    # trendYolAll = Products.objects.filter(site="Trendyol")
    # n11All = Products.objects.filter(site="n11")
    # cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
    # hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")

    # teknosaAllThread.start()
    # trendYolAllThread.start()
    # n11AllThread.start()
    # cicekSepetiAllThread.start()
    # hepsiBuradaAllThread.start()

    # teknosaAllThread.join()
    # trendYolAllThread.join()
    # n11AllThread.join()
    # cicekSepetiAllThread.join()
    # hepsiBuradaAllThread.join()


    # print("Teknosa  "+ str(len(gdwt.teknosaAll)))
    # print("Trend Yol    " + str(len(gdwt.trendYolAll)))
    # print("N11  " + str(len(gdwt.n11All)))
    # print("Cicek Sepeti     "+ str(len(gdwt.cicekSepetiAll)))
    # print("Hepsi Burda  " + str(len(gdwt.hepsiBuradaAll)))
    
    
    # allProducts = []

    # for i in gdwt.teknosaAll:

    #     equalsProduct = []
    #     equalsProduct.append(i)

    #     for j in gdwt.trendYolAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.n11All:

    #         # if j.modelNo!="Yok" and j.modelNo!="Belirtilmemiş" and j.modelNo!="" :
    #         #     if j.modelNo == i.modelNo:
    #         #         equalsProduct.append(j)
    #         #         break

    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.cicekSepetiAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.hepsiBuradaAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     if len(equalsProduct) >=2:
    #         allProducts.append(equalsProduct)
        
    
    # marka = set()
    # isletimSistemi = set()
    # islemciTipi = set()
    # islemciNesli = set()
    # ram = set()
    # diskTuru = set()
    # ekranBoyu = set()
    # diskBoyutu = set()

    # for eslesen in allProducts:

    #     for item in eslesen:

    #         if item.site == 'Teknosa':
    #             if item.marka != "":
                    
    #                 marka.add(item.marka.capitalize())

    #             if item.isletimSistemi !="":
    #                 isletimSistemi.add(item.isletimSistemi.capitalize())
                
    #             if item.islemciTipi != "":
    #                 islemciTipi.add(item.islemciTipi.title())

    #             if item.islemciNesli != "":
    #                 if(item.islemciNesli !='Yok'):
    #                     islemciNesli.add(int(item.islemciNesli))
    #                 else:
    #                     islemciNesli.add(0)
                
    #             if item.ram != "":
    #                 ram.add(int(item.ram.split(' ')[0]))
                
    #             if item.diskTuru != "":
    #                 diskTuru.add(item.diskTuru.title())
                
    #             if item.ekranBoyu != "":
    #                 ekranBoyu.add(item.ekranBoyu.capitalize())
                
    #             if item.diskBoyutu != "":
    #                 diskBoyutu.add(item.diskBoyutu.capitalize())
    #             break
    
    # marka=sorted(marka)
    # islemciNesli=sorted(islemciNesli)
    # islemciTipi=sorted(islemciTipi)
    # ekranBoyu=sorted(ekranBoyu)
    # diskBoyutu=sorted(diskBoyutu)
    # ram=sorted(ram)
    
    
    # print(type(Products.objects.filter(site="Teknosa")))
    # print("Set Marka uzunlugu "+str(len(marka)))
    # print("Sets Marka")
    # print(marka)

            


    # for eslesen in allProducts:

    #     print("Toplam eslesen "+ str(len(eslesen)))
    #     for i in eslesen:
    #         print(i.site)
    #     print("*"*100)
    

    # print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

    # for a in allProducts:
    #     for b in a:
    #         print(b.site)
    #     break
    allProducts = MatchProducts.objects.all().order_by("-puani")

    
    for i in allProducts:
        print('***********************************')
        print(i)
        print('***********************************')

    # kategorilerin ekranda sıralanmasıyla alakalı
    # model adini ekledim
    marka = set()
    modelAdi = set()
    isletimSistemi = set()
    islemciTipi = set()
    islemciNesli = set()
    ram = set()
    diskTuru = set()
    ekranBoyu = set()
    diskBoyutu = set()


    
    # kategori filter

    for item in allProducts:
 
        if item.marka != "":
            # print('')
            # print(item.marka)
            # print(item.marka.capitalize())
            # print('')
            if item.marka == "ASUS":
                marka.add(item.marka.capitalize())
            elif item.marka == "Hp":
                marka.add(item.marka.upper())
            else:
                marka.add(item.marka)
        
        if item.modelAdi !="":
            print(item.modelAdi)
            modelAdi.add(item.modelAdi)


        if item.isletimSistemi !="":
            # print('')
            # print(item.isletimSistemi)
            # print(item.isletimSistemi.capitalize())
            # print('')
            isletimSistemi.add(item.isletimSistemi)
        
        if item.islemciTipi != "":
            # print('')
            # print(item.islemciTipi)
            # print(item.islemciTipi.title())
            # print('')
            islemciTipi.add(item.islemciTipi)

        if item.islemciNesli != "":
            if(item.islemciNesli !='Yok'):
                islemciNesli.add(int(item.islemciNesli))
            else:
                islemciNesli.add(0)
            
        
        if item.ram != "":
            # print('')
            # print(item.ram)
            # print(item.ram.title())
            # print('')
            ram.add(item.ram)
        
        if item.diskTuru != "":
            # print('')
            # print(item.diskTuru)
            # print(item.diskTuru.title())
            # print('')
            diskTuru.add(item.diskTuru)
        
        if item.ekranBoyu != "":
            # print('')
            # print(item.ekranBoyu)
            # print(item.ekranBoyu.capitalize())
            # print('')
            ekranBoyu.add(item.ekranBoyu)
        
        if item.diskBoyutu != "":
            # print('')
            # print(item.diskBoyutu)
            # print(item.diskBoyutu.capitalize())
            # print('')
            diskBoyutu.add(item.diskBoyutu)
        
    

    # with open('Kategoriler.txt','w', encoding="utf-8") as f:

    #     for item in marka:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciNesli:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciTipi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ekranBoyu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskBoyutu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ram:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in isletimSistemi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskTuru:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in modelAdi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')
       
    
     
   
        
        


    marka=sorted(marka)
    islemciNesli=sorted(islemciNesli)
    islemciTipi=sorted(islemciTipi)
    ekranBoyu=sorted(ekranBoyu)
    diskBoyutu=sorted(diskBoyutu)
    ram=sorted(ram)
    
    
    # print(type(Products.objects.filter(site="Teknosa")))
    # print("Set Marka uzunlugu "+str(len(marka)))
    # print("Sets Marka")
    # print(marka)

            


    # for eslesen in allProducts:

    #     print("Toplam eslesen "+ str(len(eslesen)))
    #     for i in eslesen:
    #         print(i.site)
    #     print("*"*100)
    

    print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

    # for a in allProducts:
    #     for b in a:
    #         print(b.site)
    #     break
    posts=allProducts
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    dynamicVar = {
        'products': PostsFinal,
        'markas':marka,
        'isletimSistemis' : isletimSistemi,
        'islemciTipis' : islemciTipi,
        'islemciNeslis' : islemciNesli,
        'rams': ram,
        'diskTurus': diskTuru,
        'ekranBoyus': ekranBoyu,
        'diskBoyutus': diskBoyutu,
        'modelAdis': modelAdi    
    }
    #tum urunleri al dedik
    #tum urunleri al dedik

    #render bize gelen requeste gore templatelerden dosya arıyor
    #spesifik bir yerden aramasını istedigimizden template altında dosya olusturduk
    # return render(request, "shopping/index.html", dynamicVar) 
    return render(request, "shopping/index.html", dynamicVar)

def get_match_products():
    id=10000
    db = Database()
    db2= Database2()
    gdwt = GetDatasWithThread()    
    teknosaAllThread = threading.Thread(target=gdwt.getTeknosaAll)
    trendYolAllThread = threading.Thread(target=gdwt.getTrendYolAll)
    n11AllThread = threading.Thread(target=gdwt.getN11All)
    cicekSepetiAllThread = threading.Thread(target=gdwt.getCicekSepetiAll)
    hepsiBuradaAllThread = threading.Thread(target=gdwt.getHepsiBuradaAll)

    # teknosaAll = Products.objects.filter(site="Teknosa")
    # trendYolAll = Products.objects.filter(site="Trendyol")
    # n11All = Products.objects.filter(site="n11")
    # cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
    # hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")

    teknosaAllThread.start()
    trendYolAllThread.start()
    n11AllThread.start()
    cicekSepetiAllThread.start()
    hepsiBuradaAllThread.start()

    teknosaAllThread.join()
    trendYolAllThread.join()
    n11AllThread.join()
    cicekSepetiAllThread.join()
    hepsiBuradaAllThread.join()


    # print("Teknosa  "+ str(len(gdwt.teknosaAll)))
    # print("Trend Yol    " + str(len(gdwt.trendYolAll)))
    # print("N11  " + str(len(gdwt.n11All)))
    # print("Cicek Sepeti     "+ str(len(gdwt.cicekSepetiAll)))
    # print("Hepsi Burda  " + str(len(gdwt.hepsiBuradaAll)))

    allProducts = []

    for i in gdwt.teknosaAll:
        # print(i)
        equalsProduct = []
        equalsProduct.append(i)
        productDict = {
                'marka':i.marka,
                'modelAdi':i.modelAdi,
                'modelNo':i.modelNo,
                'isletimSistemi':i.isletimSistemi,
                'islemciTipi':i.islemciTipi,
                'islemciNesli':i.islemciNesli,
                'ram':i.ram,
                'diskBoyutu':i.ram,
                'diskTuru':i.diskTuru,
                'ekranBoyu':i.ekranBoyu,
                'puani':i.puani,
                'fiyat':i.fiyat,
                'site':i.site,
                'prodLink':i.prodLink,
                'prodImageLink':i.imageLink,
                'prodTitle':i.prodTitle,
                'prodId':i.id,
                'puani2':"",
                'fiyat2':"",
                'site2':"",
                'prodLink2':"",
                'puani3':"",
                'fiyat3':"",
                'site3':"",
                'prodLink3':"",
                'puani4':"",
                'fiyat4':"",
                'site4':"",
                'prodLink4':"",
                'puani5':"",
                'fiyat5':"",
                'site5':"",
                'prodLink5':"",
                'puani6':"",
                'fiyat6':"",
                'site6':"",
                'prodLink6':"",
                'puani6':"",
                'fiyat6':"",
                'site6':"",
                'prodLink6':"",
                'id':id
            }
        for j in gdwt.trendYolAll:
            if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
                equalsProduct.append(j)
                break
        
        for j in gdwt.n11All:

            # if j.modelNo!="Yok" and j.modelNo!="Belirtilmemiş" and j.modelNo!="" :
            #     if j.modelNo == i.modelNo:
            #         equalsProduct.append(j)
            #         break

            if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
                equalsProduct.append(j)
                break
        
        for j in gdwt.cicekSepetiAll:
            if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
                equalsProduct.append(j)
                break
        
        for j in gdwt.hepsiBuradaAll:
            if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
                equalsProduct.append(j)
                break
        
        if len(equalsProduct) >=2:
            index=1
            for m in equalsProduct:
                if(index==1):
                    index+=1
                    continue
                productDict['puani'+str(index)]=m.puani
                productDict['fiyat'+str(index)]=m.fiyat
                productDict['site'+str(index)]=m.site
                productDict['prodLink'+str(index)]=m.prodLink
                index=index+1
            db.add_one_product(productDict)
            db2.add_one_product(productDict)
            id=id+1

def AscSortProd(request):
    
    gdwt = GetDatasWithThread()

    # teknosaAllThread = threading.Thread(target=gdwt.DgetTeknosaAll)
    # trendYolAllThread = threading.Thread(target=gdwt.DgetTrendYolAll)
    # n11AllThread = threading.Thread(target=gdwt.DgetN11All)
    # cicekSepetiAllThread = threading.Thread(target=gdwt.DgetCicekSepetiAll)
    # hepsiBuradaAllThread = threading.Thread(target=gdwt.DgetHepsiBuradaAll)

    # teknosaAll = Products.objects.filter(site="Teknosa")
    # trendYolAll = Products.objects.filter(site="Trendyol")
    # n11All = Products.objects.filter(site="n11")
    # cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
    # hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")

    # teknosaAllThread.start()
    # trendYolAllThread.start()
    # n11AllThread.start()
    # cicekSepetiAllThread.start()
    # hepsiBuradaAllThread.start()

    # teknosaAllThread.join()
    # trendYolAllThread.join()
    # n11AllThread.join()
    # cicekSepetiAllThread.join()
    # hepsiBuradaAllThread.join()


    # print("Teknosa  "+ str(len(gdwt.teknosaAll)))
    # print("Trend Yol    " + str(len(gdwt.trendYolAll)))
    # print("N11  " + str(len(gdwt.n11All)))
    # print("Cicek Sepeti     "+ str(len(gdwt.cicekSepetiAll)))
    # print("Hepsi Burda  " + str(len(gdwt.hepsiBuradaAll)))
    
    
    # allProducts = []

    # for i in gdwt.teknosaAll:

    #     equalsProduct = []
    #     equalsProduct.append(i)

    #     for j in gdwt.trendYolAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.n11All:

    #         # if j.modelNo!="Yok" and j.modelNo!="Belirtilmemiş" and j.modelNo!="" :
    #         #     if j.modelNo == i.modelNo:
    #         #         equalsProduct.append(j)
    #         #         break

    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.cicekSepetiAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     for j in gdwt.hepsiBuradaAll:
    #         if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
    #             equalsProduct.append(j)
    #             break
        
    #     if len(equalsProduct) >=2:
    #         allProducts.append(equalsProduct)
        
    
    # marka = set()
    # isletimSistemi = set()
    # islemciTipi = set()
    # islemciNesli = set()
    # ram = set()
    # diskTuru = set()
    # ekranBoyu = set()
    # diskBoyutu = set()

    # for eslesen in allProducts:

    #     for item in eslesen:

    #         if item.site == 'Teknosa':
    #             if item.marka != "":
                    
    #                 marka.add(item.marka.capitalize())

    #             if item.isletimSistemi !="":
    #                 isletimSistemi.add(item.isletimSistemi.capitalize())
                
    #             if item.islemciTipi != "":
    #                 islemciTipi.add(item.islemciTipi.title())

    #             if item.islemciNesli != "":
    #                 if(item.islemciNesli !='Yok'):
    #                     islemciNesli.add(int(item.islemciNesli))
    #                 else:
    #                     islemciNesli.add(0)
                
    #             if item.ram != "":
    #                 ram.add(int(item.ram.split(' ')[0]))
                
    #             if item.diskTuru != "":
    #                 diskTuru.add(item.diskTuru.title())
                
    #             if item.ekranBoyu != "":
    #                 ekranBoyu.add(item.ekranBoyu.capitalize())
                
    #             if item.diskBoyutu != "":
    #                 diskBoyutu.add(item.diskBoyutu.capitalize())
    #             break
    
    # marka=sorted(marka)
    # islemciNesli=sorted(islemciNesli)
    # islemciTipi=sorted(islemciTipi)
    # ekranBoyu=sorted(ekranBoyu)
    # diskBoyutu=sorted(diskBoyutu)
    # ram=sorted(ram)
    
    
    # print(type(Products.objects.filter(site="Teknosa")))
    # print("Set Marka uzunlugu "+str(len(marka)))
    # print("Sets Marka")
    # print(marka)

            


    # for eslesen in allProducts:

    #     print("Toplam eslesen "+ str(len(eslesen)))
    #     for i in eslesen:
    #         print(i.site)
    #     print("*"*100)
    

    # print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

    # for a in allProducts:
    #     for b in a:
    #         print(b.site)
    #     break
    allProducts = MatchProducts.objects.all().order_by("fiyat")

    
    for i in allProducts:
        print('***********************************')
        print(i)
        print('***********************************')

    # kategorilerin ekranda sıralanmasıyla alakalı
    # model adini ekledim
    marka = set()
    modelAdi = set()
    isletimSistemi = set()
    islemciTipi = set()
    islemciNesli = set()
    ram = set()
    diskTuru = set()
    ekranBoyu = set()
    diskBoyutu = set()


    
    # kategori filter

    for item in allProducts:
 
        if item.marka != "":
            # print('')
            # print(item.marka)
            # print(item.marka.capitalize())
            # print('')
            if item.marka == "ASUS":
                marka.add(item.marka.capitalize())
            elif item.marka == "Hp":
                marka.add(item.marka.upper())
            else:
                marka.add(item.marka)
        
        if item.modelAdi !="":
            print(item.modelAdi)
            modelAdi.add(item.modelAdi)


        if item.isletimSistemi !="":
            # print('')
            # print(item.isletimSistemi)
            # print(item.isletimSistemi.capitalize())
            # print('')
            isletimSistemi.add(item.isletimSistemi)
        
        if item.islemciTipi != "":
            # print('')
            # print(item.islemciTipi)
            # print(item.islemciTipi.title())
            # print('')
            islemciTipi.add(item.islemciTipi)

        if item.islemciNesli != "":
            if(item.islemciNesli !='Yok'):
                islemciNesli.add(int(item.islemciNesli))
            else:
                islemciNesli.add(0)
            
        
        if item.ram != "":
            # print('')
            # print(item.ram)
            # print(item.ram.title())
            # print('')
            ram.add(item.ram)
        
        if item.diskTuru != "":
            # print('')
            # print(item.diskTuru)
            # print(item.diskTuru.title())
            # print('')
            diskTuru.add(item.diskTuru)
        
        if item.ekranBoyu != "":
            # print('')
            # print(item.ekranBoyu)
            # print(item.ekranBoyu.capitalize())
            # print('')
            ekranBoyu.add(item.ekranBoyu)
        
        if item.diskBoyutu != "":
            # print('')
            # print(item.diskBoyutu)
            # print(item.diskBoyutu.capitalize())
            # print('')
            diskBoyutu.add(item.diskBoyutu)
        
    

    # with open('Kategoriler.txt','w', encoding="utf-8") as f:

    #     for item in marka:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciNesli:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in islemciTipi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ekranBoyu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskBoyutu:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in ram:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in isletimSistemi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in diskTuru:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')

    #     for item in modelAdi:
    #         f.write('"')
    #         f.write(str(item))
    #         f.write('"')
    #         f.write(',')
       
    
     
   
        
        


    marka=sorted(marka)
    islemciNesli=sorted(islemciNesli)
    islemciTipi=sorted(islemciTipi)
    ekranBoyu=sorted(ekranBoyu)
    diskBoyutu=sorted(diskBoyutu)
    ram=sorted(ram)
    
    
    # print(type(Products.objects.filter(site="Teknosa")))
    # print("Set Marka uzunlugu "+str(len(marka)))
    # print("Sets Marka")
    # print(marka)

            


    # for eslesen in allProducts:

    #     print("Toplam eslesen "+ str(len(eslesen)))
    #     for i in eslesen:
    #         print(i.site)
    #     print("*"*100)
    

    print('Eslesen verilerin toplam sayısı ' + str(len(allProducts)))

    # for a in allProducts:
    #     for b in a:
    #         print(b.site)
    #     break
    posts=allProducts
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    dynamicVar = {
        'products': PostsFinal,
        'markas':marka,
        'isletimSistemis' : isletimSistemi,
        'islemciTipis' : islemciTipi,
        'islemciNeslis' : islemciNesli,
        'rams': ram,
        'diskTurus': diskTuru,
        'ekranBoyus': ekranBoyu,
        'diskBoyutus': diskBoyutu,
        'modelAdis': modelAdi    
    }
    #tum urunleri al dedik
    #tum urunleri al dedik

    #render bize gelen requeste gore templatelerden dosya arıyor
    #spesifik bir yerden aramasını istedigimizden template altında dosya olusturduk
    # return render(request, "shopping/index.html", dynamicVar) 
    return render(request, "shopping/index.html", dynamicVar)