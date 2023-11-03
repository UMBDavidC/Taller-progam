from django.urls import path
from . import views

urlpatterns = [
    path('agregar_testimonio/', views.agregar_testimonio, name='agregar_testimonio'),
    path('Reseñas/', views.testimonio, name='Reseñas'),
    # Más entradas de URL
]