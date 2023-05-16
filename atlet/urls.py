
from django.urls import path
from atlet.views import daftar_stadium

app_name = 'atlet'

urlpatterns = [
    path('daftar-event/', daftar_stadium, name='daftar_stadium'),
]