def enrolled_events(request):
    atlet = request.user.atlet 
    enrollments = Enrollment.objects.filter(atlet=atlet)
    return render(request, 'enrolled_events.html', {'enrollments': enrollments})
def unenroll_event(request, enrollment_id):
    enrollment = Enrollment.objects.get(pk=enrollment_id)
    enrollment.delete()
    return redirect('enrolled_events')


