from django.shortcuts import render
from .models import EnrolledEvent, Match

def show_results(request, event_id):
    event = EnrolledEvent.objects.get(id=event_id)
    matches = Match.objects.filter(event=event)
    return render(request, 'result.html', {'event': event, 'matches': matches})
