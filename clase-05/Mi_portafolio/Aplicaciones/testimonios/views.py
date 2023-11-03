from django.shortcuts import render, redirect
from .models import Testimonio

def agregar_testimonio(request):
    if request.method == "POST":
        tname = request.POST["name"]
        tmessage = request.POST["message"]

        if tname and tmessage:
            obj_testi = Testimonio(nombre=tname, testimonio=tmessage)
            obj_testi.save()
            return render(request,"gracias.html",)

    return render(request, 'agregar_testimonio.html')

def testimonio(request):
    mis_reseñas = Testimonio.objects.all()
    return render(request,"Reseñas.html",{"testimonios": mis_reseñas})




