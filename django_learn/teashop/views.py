from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    
    p = Product()
    p.title = "Sunflower tea"
    p.price = 50
    
    # return HttpResponse("<h1>Hello World</h1>")
    # return render(request,'index.html')
    return render(request,'index.html',{"p1": p}) 
