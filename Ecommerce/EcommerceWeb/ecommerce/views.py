from django.shortcuts import render
from .models import Prods


def homepage(request):
    prod= {
        "prods": Prods.objects.all()
    }     
    return render(request,'ecommerce/home.html',prod)
