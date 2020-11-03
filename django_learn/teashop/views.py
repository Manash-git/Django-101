from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    # load data from database
    prdcts = Product.objects.all()
    
    
    # below for load data from pc
    '''
    p1 = Product()
    p1.title = "Sunflower tea"
    p1.price = 70
    p1.img = 'product-1.jpeg'
    p1.offer = False
    
    p2 = Product()
    p2.title = "Lemon Tea"
    p2.price = 50
    p2.img = 'product-2.jpeg'
    p2.offer = False
    
    p3 = Product()
    p3.title = "Masala tea"
    p3.price = 100
    p3.img = 'product-3.jpeg'
    p3.offer = True
    
    prdcts = [p1,p2,p3]
    '''
    # return HttpResponse("<h1>Hello World</h1>")
    # return render(request,'index.html')
    return render(request,'index.html',{"prdcts":prdcts}) 
