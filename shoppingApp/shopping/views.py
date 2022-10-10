from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# burada beliritilen linklerde neler gozukecegini soyleriz


def home(request):

    #render bize gelen requeste gore templatelerden dosya arıyor
    #spesifik bir yerden aramasını istedigimizden template altında dosya olusturduk
    return render(request, "shopping/index.html") 

def productDetails(request, id):

    # mesela biz id yi de request gondermek istiyoruz
    # onu bir dict yapısında 3. parametre olarak gonderebilirz
    # ilgili yerde kullanımı {{ }} icersinde olur
    dynamicVar = {
        'id':id
    }
    return render(request, "shopping/productDetails.html", dynamicVar)
