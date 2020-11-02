from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    # return render(request,'index.html')
    return render(request,'index.html',{'name':'manash'})

def addition(request):
    val1 = int(request.GET['num1'])
    # val1 = request.GET['num1']
    val2 = int(request.GET["num2"])
    res = val1+val2
    # return render(request, 'result.html')
    return render(request, 'result.html',{"result":res})