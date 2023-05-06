from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('enrolled-events/', views.enrolled_events, name='enrolled_events'),
]
