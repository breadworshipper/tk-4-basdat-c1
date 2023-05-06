from django.urls import path
from reg_log.views import login
from reg_log.views import portal
from reg_log.views import register
from reg_log.views import register_athlete
from reg_log.views import register_coach
from reg_log.views import register_umpire
app_name = 'reg_log'
urlpatterns = [
    path('portal/', portal, name = 'portal'),
    path('portal/login/', login, name='login'),
    path('portal/register/', register, name='register'),
    path('portal/register/atlet', register_athlete, name='register'),
    path('portal/register/pelatih', register_coach, name='register'),
    path('portal/register/umpire', register_umpire, name='register'),

]