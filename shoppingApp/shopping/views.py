from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
import threading
# tablodaki verileri cekip canlıya atmak icin

# Create your views here.
# burada beliritilen linklerde neler gozukecegini soyleriz





class GetDatasWithThread:

    # teknosaAll=[]
    # trendYolAll=[]
    # n11All=[]
    # cicekSepetiAll=[]
    # hepsiBuradaAll=[]

    def __init__(self) -> None:
        pass

    def getTeknosaAll(self):
        print('Teknosa cekerim')
        self.teknosaAll = Products.objects.filter(site="Teknosa")

    def getTrendYolAll(self):
        print('Trendyol cekerim')
        self.trendYolAll = Products.objects.filter(site="Trendyol")

    def getN11All(self):
        print('N11 cekerim')
        self.n11All = Products.objects.filter(site="n11")

    def getCicekSepetiAll(self):
        print('Cicek cekerim')
        self.cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
       
    def getHepsiBuradaAll(self):
        print('Hepsi cekerim')
        self.hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")



def home(request):

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

    print("Teknosa  "+ str(len(gdwt.teknosaAll)))
    print("Trend Yol    " + str(len(gdwt.trendYolAll)))
    print("N11  " + str(len(gdwt.n11All)))
    print("Cicek Sepeti     "+ str(len(gdwt.cicekSepetiAll)))
    print("Hepsi Burda  " + str(len(gdwt.hepsiBuradaAll)))
    
    
    allProducts = []

    for i in gdwt.teknosaAll:

        equalsProduct = []
        equalsProduct.append(i)

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
            allProducts.append(equalsProduct)
        
    

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
    
    dynamicVar = {
        'products': allProducts
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

    product = Products.objects.get(id=id)

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
