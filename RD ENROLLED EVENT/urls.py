from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('enrolled-events/', views.enrolled_events, name='enrolled_events'),
    path('unenroll-event/<int:enrollment_id>/', views.unenroll_event, name='unenroll_event'),
]
