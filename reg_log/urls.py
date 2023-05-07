from django.urls import path
from reg_log.views import login
from reg_log.views import portal
from reg_log.views import register
from reg_log.views import register_athlete
from reg_log.views import register_coach
from reg_log.views import register_umpire
app_name = 'reg_log'
urlpatterns = [
    path('register/umpire', register_umpire, name='register-umpire'),
    path('', portal, name = 'portal'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('register/atlet', register_athlete, name='register-atlet'),
    path('register/pelatih', register_coach, name='register-coach'),
    

]