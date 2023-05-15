from django.shortcuts import render, redirect
from .forms import QualificationForm
from .models import UjianKualifikasi

def qualification_view(request):
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.atlet = request.user.atlet  
            qualification.save()
            return redirect('question_view', qualification_id=qualification.pk)
    else:
        form = QualificationForm()
    return render(request, 'qualification.html', {'form': form})

def question_view(request, qualification_id):
    qualification = Qualification.objects.get(pk=qualification_id)
    questions = UjianKualifikasi.objects.filter(qualification=qualification)
    if request.method == 'POST':
        
        total_correct_answers = 0
        for question in questions:
            user_answer = request.POST.get(str(question.pk))
            if user_answer == question.correct_choice:
                total_correct_answers += 1
        if total_correct_answers >= 4:
            qualification.atlet.status = 'Qualified'
            qualification.atlet.world_rank = 1  
            qualification.atlet.save()
        return redirect('dashboard')  
    return render(request, 'questions.html', {'questions': questions})
