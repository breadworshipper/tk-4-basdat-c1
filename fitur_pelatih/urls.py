from django.urls import path
from fitur_pelatih.views import daftar_atlet
from fitur_pelatih.views import list_atlet

app_name = 'fitur_pelatih'
urlpatterns = [
    path('list-atlet/', list_atlet, name = 'list_atlet'),
    path('daftar-atlet/', daftar_atlet, name = 'daftar_atlet'),
    
]