from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def terminos(request):
    return render(request,"pages/terminos.html",{})

def privacidad(request):
    return render(request,"pages/privacidad.html",{})

@login_required
def resumen(request):
    return render(request,"pages/resumen.html",{})

def inicio(request):
    return render(request,"pages/index.html",{})

def login(request):
    return render(request,"pages/login.html",{})

