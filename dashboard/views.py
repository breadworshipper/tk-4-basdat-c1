from django.shortcuts import render


def dashboard_umpire(request):
    return render(request, 'umpire.html')
def dashboard_pelatih(request):
    return render(request, 'pelatih.html')
def dashboard_atlet(request):
    return render(request, 'atlet.html')

