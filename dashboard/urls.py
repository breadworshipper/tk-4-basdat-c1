from django.urls import path
from dashboard.views import dashboard_atlet
from dashboard.views import dashboard_pelatih
from dashboard.views import dashboard_umpire
app_name = 'dashboard'
urlpatterns = [
    path('umpire/', dashboard_umpire, name = 'd_umpire'),
    path('atlet/', dashboard_atlet, name = 'd_atlet'),
    path('pelatih/', dashboard_pelatih, name = 'd_pelatih'),
]