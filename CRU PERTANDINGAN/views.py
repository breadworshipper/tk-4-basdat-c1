from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import EnrolledEvent, Match

def start_match(request, event_id):
    event = EnrolledEvent.objects.get(id=event_id)
    event.is_started = True
    event.save()
    matches = Match.objects.filter(event=event)
    return render(request, 'match.html', {'event': event, 'matches': matches})

def match_done(request):
    return HttpResponseRedirect('/hasil-pertandingan/')  
