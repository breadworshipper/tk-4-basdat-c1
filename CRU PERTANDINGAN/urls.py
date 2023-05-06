from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('start-match/<int:event_id>/', views.start_match, name='start_match'),
    path('match-done/', views.match_done, name='match_done'),
]
