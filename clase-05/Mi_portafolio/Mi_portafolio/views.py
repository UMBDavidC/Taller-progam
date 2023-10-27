from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def resumen(request):
    return render(request,"pages/resumen.html",{})

def inicio(request):
    return render(request,"pages/index.html",{})

def login(request):
    return render(request,"pages/login.html",{})