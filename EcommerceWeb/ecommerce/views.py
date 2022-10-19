import re
from django.shortcuts import render
from .models import Prods


def homepage(request):
    prod= {
        "prods": Prods.objects.all()
    } 
    return render(request,'ecommerce/home.html',prod)

def prodDetails(request,id):
    prod={
        "prods": Prods.objects.get(id=id)
    }
    return render(request,'ecommerce/details.html',prod)
    
def DescSortProd(request):
    
    prod={
        "prods": Prods.objects.all().order_by('-fiyat').values
    }
    return render (request,'ecommerce/home.html',prod)

def AscSortProd(request):
    
    prod={
        
        "prods":Prods.objects.all().order_by('fiyat').values
    }
    return render(request,'ecommerce/home.html',prod)

def prodStarSort(request):
    
    prod={
        
        "prods": Prods.objects.all().order_by('-puani').values
    }
    
    return render(request,'ecommerce/home.html',prod)