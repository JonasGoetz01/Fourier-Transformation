from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mainview-home'), #Die Umleitung von der project views datei führt hierher; die Anfrage wird von der Funktion home() in der views Datei ausgeführt
    path('about/', views.about, name='mainview-about'), #Umleitung an views.py und darin wird die Funktion about() angesprochen

]