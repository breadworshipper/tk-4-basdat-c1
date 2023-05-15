from django.urls import path
from . import views

urlpatterns = [
    path('hasil-pertandingan/<int:event_id>/', views.show_results, name='show_results'),
]
