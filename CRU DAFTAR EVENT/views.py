from django.shortcuts import render, redirect
from .models import Stadium, Event, Registration
from .forms import RegistrationForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def select_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.atlet = request.user.atlet  # Sesuaikan dengan model atlet Anda
            registration.save()
            return redirect('select_category', registration_id=registration.pk)
    else:
        form = RegistrationForm()
    return render(request, 'select_event.html', {'event': event, 'form': form})

def select_category(request, registration_id):
    registration = Registration.objects.get(pk=registration_id)
    event = registration.event
    atlet = registration.atlet
    if request.method == 'POST':
        category = request.POST.get('category')
        partner = request.POST.get('partner')
        registration.category = category
        if category == 'Ganda':
            registration.partner = partner
        registration.save()
        return redirect('enrolled_events')  
    else:
       
        if atlet.gender == 'Laki-laki':
            if event.category == 'Ganda Putra':
                partner_category = 'Laki-laki'
            else:
                partner_category = 'Perempuan'
            partner_dropdown = Atlet.objects.filter(gender=partner_category).exclude(registration__event=event, registration__partner__isnull=False)
        else:
            if event.category == 'Ganda Putri':
                partner_category = 'Perempuan'
            else:
                partner_category = 'Laki-laki'
            partner_dropdown = Atlet.objects.filter(gender=partner_category).exclude(registration__event=event, registration__partner__isnull=False)
    return render(request, 'select_category.html', {'event': event, 'registration': registration, 'partner_dropdown': partner_dropdown})
