from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_umpire(request):
    return render(request, 'umpire.html')

def register_athlete(request):
    return render(request, 'athlete.html')

def register_coach(request):
    return render(request, 'coach.html')

def portal(request):
    return render(request, 'portal.html')