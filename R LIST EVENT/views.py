from django.shortcuts import render
from .models import EnrolledEvent

def enrolled_events(request):
    enrolled_events = EnrolledEvent.objects.filter(atlet=request.user.atlet)  

    return render(request, 'enrolled_events.html', {'enrolled_events': enrolled_events})
