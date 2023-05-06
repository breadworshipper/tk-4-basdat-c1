from django.urls import path
from reg_log.views import login
from reg_log.views import portal
from reg_log.views import register

app_name = 'reg_log'
urlpatterns = [
    path('portal/', portal, name = 'portal'),
    path('portal/login/', login, name='login'),
    path('portal/register/', register, name='register'),
]