from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# burada beliritilen linklerde neler gozukecegini soyleriz


def home(request):
    return HttpResponse("Home Page")

def productDetail(request, id):
    return HttpResponse("Product Detail id : {}".format(id))
