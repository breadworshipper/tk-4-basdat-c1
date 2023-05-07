from django.shortcuts import render


def dashboard_umpire(request):
    return render(request, 'dashboard_umpire.html')
def dashboard_pelatih(request):
    return render(request, 'dashboard_pelatih.html')
def dashboard_atlet(request):
    return render(request, 'dashboard_atlet.html')

