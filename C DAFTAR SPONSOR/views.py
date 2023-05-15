from django.shortcuts import render, redirect
from .models import SponsorRegistration

def sponsor_registration(request):
    if request.method == 'POST':
        nama_sponsor = request.POST.get('nama_sponsor')
        tanggal_mulai = request.POST.get('tanggal_mulai')
        tanggal_selesai = request.POST.get('tanggal_selesai')

  
        sponsor_registration = SponsorRegistration(
            atlet=request.user.atlet,  
            nama_sponsor=nama_sponsor,
            tanggal_mulai=tanggal_mulai,
            tanggal_selesai=tanggal_selesai
        )
        sponsor_registration.save()

        return redirect('sponsor_registration')  

    return render(request, 'sponsor_registration.html')
