from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('sponsor-registration/', views.sponsor_registration, name='sponsor_registration'),
]