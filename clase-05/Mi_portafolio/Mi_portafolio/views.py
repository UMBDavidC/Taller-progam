from django.shortcuts import render

def inicio(request):
    return render(request,"pages/index.html",{})

def resumen(request):
    return render(request,"pages/resumen.html",{})