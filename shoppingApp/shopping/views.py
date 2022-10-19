from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
# tablodaki verileri cekip canlıya atmak icin

# Create your views here.
# burada beliritilen linklerde neler gozukecegini soyleriz


def home(request):

    teknosaAll = Products.objects.filter(site="Teknosa")
    trendYolAll = Products.objects.filter(site="Trendyol")
    n11All = Products.objects.filter(site="n11")
    cicekSepetiAll = Products.objects.filter(site="ÇiçekSepeti")
    hepsiBuradaAll = Products.objects.filter(site="Hepsiburada")

    print("Teknosa  "+ str(len(teknosaAll)))
    print("Trend Yol    " + str(len(trendYolAll)))
    print("N11  " + str(len(n11All)))
    print("Cicek Sepeti     "+ str(len(cicekSepetiAll)))
    print("Hepsi Burda  " + str(len(hepsiBuradaAll)))
    
    
    allProducts = []

    for i in teknosaAll:

        equalsProduct = []
        equalsProduct.append(i)

        for j in trendYolAll:
            if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
                equalsProduct.append(j)
                break
        
        for j in n11All:

            # if j.modelNo!="Yok" and j.modelNo!="Belirtilmemiş" and j.modelNo!="" :
            #     if j.modelNo == i.modelNo:
            #         equalsProduct.append(j)
            #         break

            if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
                equalsProduct.append(j)
                break
        
        for j in cicekSepetiAll:
            if j.prodTitle.lower().find(i.modelNo.lower()) !=-1:
                equalsProduct.append(j)
                break
        
        for j in hepsiBuradaAll:
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

    for a in allProducts:
        for b in a:
            print(b.site)
        break
    
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
