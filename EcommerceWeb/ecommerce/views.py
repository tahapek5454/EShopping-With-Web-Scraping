import re
from django.shortcuts import render
from .models import Prods
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache


def get_data():
    
    posts=[]
    db=None
    
    if(cache.get('products')):
        posts=cache.get('products')
        print('Redis')
    else: 
        prods=Prods.objects.all()
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
        prods=Prods.objects.all().order_by('fiyat')
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
        prods=Prods.objects.all().order_by('-fiyat')
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
        prods=Prods.objects.all().order_by('-puani')
        for prod in prods:
            posts.append(prod)
        print('sqlite')
        
        cache.set('stars',posts)
    
    return posts

def homepage(request):

    posts = get_data()
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)

def prodDetails(request,id):
    
    if(cache.get(id)):
        product=cache.get(id)   
        print('Hit the cache')
    else:
        try:
            product=Prods.objects.get(id=id)
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

def prodStarSort(request):
    posts=get_star_data()
    page = request.GET.get('page')
    num_of_item= 20
    paginator= Paginator(posts,num_of_item)
    PostsFinal=paginator.get_page(page)
    
    
    
    prod={'prods':PostsFinal,'paginator':paginator}
    
    return render(request,'ecommerce/home.html',prod)
