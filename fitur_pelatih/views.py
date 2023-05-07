from django.shortcuts import render


def list_atlet(request):
    return render(request,'list_atlet.html')
def daftar_atlet(request):
    return render(request,'daftar_atlet.html')


# Create your views here.
