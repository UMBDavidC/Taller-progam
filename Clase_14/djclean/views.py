from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"pages/index.html",{})

def nosotros(request):
    return render(request,"pages/otro.html",{})