import re
from django.shortcuts import render
from .models import Prods
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache


def homepage(request):

    
    posts=Prods.objects.all()
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)

def prodDetails(request,id):
    prod={
        "prods": Prods.objects.get(id=id)
    }
    return render(request,'ecommerce/details.html',prod)
    
def DescSortProd(request):
    posts=Prods.objects.all().order_by('-fiyat')
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)



def AscSortProd(request):
    posts=Prods.objects.all().order_by('fiyat')
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)

def prodStarSort(request):
    
    posts=Prods.objects.all().order_by('-puani')
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)
