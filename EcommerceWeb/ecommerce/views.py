import re
from django.shortcuts import render, redirect
from .models import MatchProducts
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache
import pymongo

def get_data():
    
    posts=[]
    db=None
    
    if(cache.get('products')):
        posts=cache.get('products')
        print('Redis')
    else: 
        prods=MatchProducts.objects.all()
        for prod in prods:
            posts.append(prod)
        print('sqlite')
        
        cache.set('products',posts)
    
    return posts

def asc_get_price_data():
    
    posts=[]
    db=None
    
    if(cache.get('asc_products')):
        posts=cache.get('asc_products')
        print('Redis')
    else: 
        prods=MatchProducts.objects.all().order_by('fiyat')
        for prod in prods:
            posts.append(prod)
        print('sqlite')
        
        cache.set('asc_products',posts)
    
    return posts

def desc_get_price_data():
    
    posts=[]
    db=None
    
    if(cache.get('desc_products')):
        posts=cache.get('desc_products')
        print('Redis')
    else: 
        prods=MatchProducts.objects.all().order_by('-fiyat')
        for prod in prods:
            posts.append(prod)
        print('sqlite')
        
        cache.set('desc_products',posts)
    
    return posts

def get_star_data():
    
    posts=[]
    db=None
    
    if(cache.get('stars')):
        posts=cache.get('stars')
        print('Redis')
    else: 
        prods=MatchProducts.objects.all().order_by('-puani')
        for prod in prods:
            posts.append(prod)
        print('sqlite')
        
        cache.set('stars',posts)
    
    return posts

def homepage(request):




    allProducts = get_data()

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
            #print(item.modelAdi)
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
        'prods': PostsFinal,
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
    
    return render(request,'ecommerce/home.html',dynamicVar)

def prodDetails(request,id):
    
    if(cache.get(id)):
        product=cache.get(id)   
        print('Hit the cache')
    else:
        try:
            product=MatchProducts.objects.get(id=id)
            cache.set(id,product)
            print('Hit the db')
        except:
            print('Cannot find!')
    prod={
        "prods": product
    }
    return render(request,'ecommerce/details.html',prod)
    
def DescSortProd(request):
    posts=desc_get_price_data()
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)

def AscSortProd(request):
    posts=asc_get_price_data()
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)


def filterByCategory(request):
    
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
        
        

    print(base)

    if flag:
        
        
        # baglanma islemi
        myClient = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']


        myCollection = mydb['ecommerce_matchproducts']

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
            # posts=allProducts
            # page = request.GET.get('page')
            # num_of_item= 20
            # paginator= Paginator(posts,num_of_item)
            # PostsFinal=paginator.get_page(page)
            
            dynamicVar = {
                'prods': allProducts,
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
            return render(request, "ecommerce/home.html", dynamicVar)

            

    else:
        return redirect('home')

def filterWithSearchBar(request):
    
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
        

    print(base)

    if flag:
        
        
        # baglanma islemi
        myClient = pymongo.MongoClient('mongodb://abvag:abvag@localhost:27017')

        # database e gimre
        mydb = myClient['WebScraping']


        myCollection = mydb['ecommerce_matchproducts']

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
                'prods': PostsFinal,
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
            return render(request, "ecommerce/home.html", dynamicVar)

            

    else:
        return redirect('home')

def prodStarSort(request):
    posts=get_star_data()
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)
